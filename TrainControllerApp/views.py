from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Command, Train
import re
from .business import Controller

# Init controller (ugly way to do it)
controller = Controller()

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def dashboard(request):
    if request.user.is_authenticated:
        context = {}
        context['trains'] = request.user.trains()
        return render(request, 'dashboard.html', context)
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def about(request):
    context = {}
    return render(request, 'about.html', context)

# -------------------------------- #
# ------------ Trains ------------ #
# -------------------------------- #
def train_new(request):
    ''' display a form allowing user to register a new train '''
    if request.user.is_authenticated:
        context = {}
        return render(request, 'trains/newedit.html', context)
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def train_register(request):
    ''' Register a new train '''
    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user

        # Get and validate train name
        train_name = request.POST.get('input_name')
        if not re.match('^[a-zA-Z0-9_]+$', train_name):
            messages.error(request, "Invalid name ! Must be alphanumerical")
            return redirect('trains.new')

        # Get and validate train name
        train_lokid = request.POST.get('input_lokid')
        if not re.match('(^[0-9]{1,4}$)', train_lokid):
            messages.error(request, "Invalid lokid ! Must be between 0 and 9999 inclusive")
            return redirect('trains.new')

        new_train = Train()
        new_train.name = train_name
        new_train.lokid = train_lokid
        new_train.user = user
        new_train.save()

        messages.success(request, "New train succefully registrated !")
        return redirect('trains.gallery')
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def train_edit(request, train_id):
    ''' display a form allowing user to edit a train '''
    if request.user.is_authenticated:
        if train_id.isdigit() and int(train_id) >= 0:
            context = {}
            context['train'] = get_object_or_404(Train, id=train_id)
            return render(request, 'trains/newedit.html', context)
        else:
            messages.error(request, "Invalid train id !")
            return redirect('/')
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def train_update(request, train_id):
    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user

        # Get and validate train name
        train_name = request.POST.get('input_name')
        if not re.match('^[a-zA-Z0-9_]+$', train_name):
            messages.error(request, "Invalid name ! Must be alphanumerical")
            return redirect('trains.edit', train_id=train_id)

        # Get and validate train name
        train_lokid = request.POST.get('input_lokid')
        if not re.match('^[0-9]{4}+$', train_lokid):
            messages.error(request, "Invalid lokid ! Must be between 0 and 9999 inclusive")
            return redirect('trains.edit', train_id=train_id)

        if train_id.isdigit() and int(train_id) >= 0:
            new_train = Train.objects.get(train_id)
            new_train.name = train_name
            new_train.lokid = train_lokid
            new_train.user = user
            new_train.save()
        else:
            messages.error(request, "Invalid train id !")
            return redirect('trains.edit', train_id=train_id)

        messages.success(request, "New train succefully registrated !")
        return redirect('trains.gallery')
    else:
        messages.error(request, "Login first !")
        return redirect('/')


def train_delete(request, train_id):
    pass

def train_gallery(request):
    ''' display user's train '''
    if request.user.is_authenticated:
        context = {}
        context['trains'] = request.user.trains()
        return render(request, 'trains/gallery.html', context)
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def train_show(request, train_id):
    ''' display user's train '''
    if request.user.is_authenticated:
        if train_id.isdigit() and int(train_id) >= 0:
            context = {}
            context['train'] = Train.objects.get(id=train_id)
            return render(request, 'trains/show.html', context)
        else:
            messages.error(request, "Invalid train id !")
            return redirect('trains.gallery')

    else:
        messages.error(request, "Login first !")
        return redirect('/')
    pass

# ---------------------------------- #
# ------------ Commands ------------ #
# ---------------------------------- #

def command_gallery(request):
    ''' display every supported command to the user '''
    context = {}
    context['commands'] = Command.objects.all()
    return render(request, 'commands/gallery.html', context)

def command_show(request, command_id):
    ''' display the command's page to the user '''
    if command_id.isdigit() and int(command_id) >= 0:
        context = {}
        context['command'] = get_object_or_404(Command, id=command_id)
        return render(request, 'commands/show.html', context)
    else:
        messages.error(request, "Invalid command id !")
        return redirect('/')

# --------------------------------------- #
# ------------ Control Panel ------------ #
# --------------------------------------- #
def control_panel(request):
    if request.user.is_authenticated:
        context = {}
        # TODO: Fetch trains, commands etc

        return render(request, 'panels/control.html', context)
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def control_process(request):
    import json

    if request.user.is_authenticated and request.method == 'POST':
        #try:

        # Fetch JSON
        data = request.POST.get('json')
        data = json.loads(data)

        # Validate action
        action = data.get('action')
        if not re.match('^[a-z]+$', action):
            messages.error(request, "Invalid train_id !")
            return HttpResponseBadRequest("Bad command provided")

        # Get args
        args = data.get('args')

        # Validate train_id
        train_id = args.get('id')
        if train_id is not None and not re.match('^[0-9]{4}$', train_id):
            messages.error(request, "Invalid train_id !")
            return HttpResponseBadRequest("Bad command provided")
        
        # Process action
        controller.process(action, args)

        # Read from Intellibox
        return HttpResponse(controller.readResponse())
            
        # except:
        #     messages.error(request, "An error occured while processing command !")
        #     return HttpResponseBadRequest("Something went wrong !")
    else:
        messages.error(request, "Login first !")
        return redirect('/')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Command, Train

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def dashboard(request):
    pass

def about(request):
    context = {}
    return render(request, 'about.html', context)

# -------------------------------- #
# ------------ Trains ------------ #
# -------------------------------- #
def train_new(request):
    ''' display a page to the user allowing him to create a new train entry '''
    if request.user.is_authenticated:
        context = {}
        return render(request, 'trains/newedit.html', context)
    else:
        messages.error(request, "Login first !")
        return redirect('/')


def train_register(request):
    pass

def train_edit(request, train_id):
    ''' display a page to the user allowing him to update a train '''
    if request.user.is_authenticated:
        if train_id.isdigit() and int(train_id) >= 0:
            context = {}
            context['train'] = get_object_or_404(Train, id=train_id)
            return render(request, 'trains/newedit.html', context)
        else:
            messages.error(request, "Invalid command id !")
            return redirect('/')
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def train_update(request, train_id):
    pass

def train_delete(request, train_id):
    pass

def train_gallery(request):
    ''' Display every train registred by user '''
    if request.user.is_authenticated:
        context = {}
        context['trains'] = request.user.profile.trains.all()
        return render(request, 'trains/gallery.html', context)
    else:
        messages.error(request, "Login first !")
        return redirect('/')

def train_show(request, train_id):
    ''' display the train's page to the user '''
    if request.user.is_authenticated:
        if train_id.isdigit() and int(train_id) >= 0:
            context = {}
            context['train'] = get_object_or_404(Command, id=train_id)
            return render(request, 'trains/show.html', context)
        else:
            messages.error(request, "Invalid train id !")
            return redirect('/')
    else:
        messages.error(request, "Login first !")
        return redirect('/')

# ---------------------------------- #
# ------------ Commands ------------ #
# ---------------------------------- #

def command_gallery(request):
    ''' Display supported command to the user '''
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

def control_train(request, train_id, command_id):
    if request.user.is_authenticated:
        context = {}

        # TODO: Fetch parameters
        pass
    else:
        messages.error(request, "Login first !")
        return redirect('/')


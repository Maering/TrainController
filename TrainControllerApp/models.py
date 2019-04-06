from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# ---------------------------------- #
# ------------ Hardware ------------ #
# ---------------------------------- #
class Baudrate(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField()

class SerialPort(models.Model):
    id = models.AutoField(primary_key=True)
    baudrate = models.ForeignKey(Baudrate, on_delete=models.CASCADE)
    parity = models.PositiveSmallIntegerField()

# ---------------------------------- #
# ------------ Software ------------ #
# ---------------------------------- #
class Train(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    lokid = models.PositiveSmallIntegerField(unique=True) # 0 to 32767
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user', null=True)
    # TODO: parameters are handled at runtime (speed, direction, light, functions, etc...)

class Command(models.Model):
    ''' class representing a command for Intellibox '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    p50xa = models.CharField(max_length=100, unique=True)
    p50xb = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    hasparams = models.BooleanField(default=False)
    # TODO: parameters are handled at runtime 
    # TODO: handle return off the command

# ------------------------------------ #
# ------------ Extensions ------------ #
# ------------------------------------ #
def trains(self):
    return Train.objects.filter(user=self)
auth.models.User.add_to_class('trains', trains)


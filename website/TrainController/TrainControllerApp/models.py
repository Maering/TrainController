from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

# ----------------------------------------- #
# ------------ User extensions ------------ #
# ----------------------------------------- #
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trains = models.ManyToManyField(Train, related_name='trains')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
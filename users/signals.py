# Done so that every user has a profile created for them when they are created, instead of assigning them profile picture on the django administration page

from django.db.models.signals import post_save      # Signal Fired when an object is saved
from django.contrib.auth.models import User         # Because we want to fire signal after user is created
from django.dispatch import receiver                # Function which receives signal and performs some task
from .models import Profile                         # Importing Profile model

@receiver(post_save, sender=User)                           # When a user is saved, send this signal
def create_profile(sender, instance, created, **kwargs):    # create_profile is a receiver function
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)                   
def save_profile(sender, instance, created, **kwargs):    
    instance.profile.save()                                 # Save the profile of the user

# Now we just have to import this signals.py file in the apps.py file of the users app

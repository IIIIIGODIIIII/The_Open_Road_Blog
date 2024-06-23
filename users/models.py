from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# In Django, whenever you make changes to your models (e.g., adding a new field, changing a field type, 
# removing a field, etc.), you need to create and apply migrations to reflect these changes in your database schema.

# Create your models here.

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)                # OneToOneField creates one to one matching which means that one user will have one profile and one profile will have one user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # default.jpg is the default image that will be displayed if no image is uploaded

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()                       # To use save() method of parent class we use super()
        img = Image.open(self.image.path)    # Open the image of the current instance
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)         # Set the size of the image to 300x300
            img.thumbnail(output_size)       # Resize the image to 300x300
            img.save(self.image.path)        # Save the image to the path of the current instance
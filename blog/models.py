from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# In Django, whenever you make changes to your models (e.g., adding a new field, changing a field type, 
# removing a field, etc.), you need to create and apply migrations to reflect these changes in your database schema.

# Create your models here.

# Each class is a table in the database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)        # automatically set to the current date and time.
    author = models.ForeignKey(User, on_delete=models.CASCADE)      # if the user is deleted, delete the post as well

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})      # This will return the URL as a string to the post that was created
    
    
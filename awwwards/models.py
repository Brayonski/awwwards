from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    location = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    profile_pic = models.ImageField()
    bio = models.TextField()
    contact = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.profile_pic

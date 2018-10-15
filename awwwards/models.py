from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    profile_pic = models.ImageField()
    bio = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.profile_pic

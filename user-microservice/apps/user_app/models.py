import email
from django.db import models
from django.contrib.auth.models import AbstractUser

# Models of program and User profile
class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    google_id = models.CharField(max_length=255, unique=True)
    picture = models.URLField(max_length=255, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)
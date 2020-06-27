from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
  text = models.TextField('Bio')
  picture = models.ImageField('Avatar', default='default.png')
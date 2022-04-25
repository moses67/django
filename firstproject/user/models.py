from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField (default = 'Default.png', upload_to = 'passport')

    def __str__(self):
        return f'{self.user.username} profile'
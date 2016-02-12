from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserRegistrationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField('registration date', default=timezone.now)
    activation_code = models.CharField(max_length=100, default=None)
    activation_date = models.DateTimeField('validation date', default=timezone.now)

    def __str__(self):
        return self.user.username


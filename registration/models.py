from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class UserRegistrationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField('registration date', default=timezone.now)
    activation_date = models.DateTimeField('validation date', default=timezone.now)

    def __str__(self):
        return self.user.username


class UserPreRegistration(models.Model):
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=False,unique=True,
                              error_messages={
                                    'unique': _("A user with that username already exists."),
                                })
    password = models.CharField(max_length=50, default="test")
    registration_date = models.DateTimeField(_('registration date'), default=timezone.now)
    activation_code = models.CharField(max_length=100, default=None)
    activation_Date = models.DateTimeField('validation date', default=timezone.now)

    def __str__(self):
        return self.username
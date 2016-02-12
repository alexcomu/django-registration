from .models import UserRegistrationInfo
from django.contrib import admin


class UserRegistrationInfoAdmin(admin.ModelAdmin):
    fields = ['user', 'registration_date', 'activation_date']

admin.site.register(UserRegistrationInfo, UserRegistrationInfoAdmin)



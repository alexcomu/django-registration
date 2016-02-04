from .models import UserRegistrationInfo, UserPreRegistration
from django.contrib import admin


class UserRegistrationInfoAdmin(admin.ModelAdmin):
    fields = ['user', 'registration_date', 'activation_date']

class UserPreRegistrationAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'registration_date','activation_code')

admin.site.register(UserRegistrationInfo, UserRegistrationInfoAdmin)
admin.site.register(UserPreRegistration, UserPreRegistrationAdmin)



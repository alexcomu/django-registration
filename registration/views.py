from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django import forms

#  **********************************************************
#  *  Validators                                            *
#  **********************************************************

def post_validator(callback):
    '''
    Post Validator Function. Check Email - Password and username
    :param callback:
    :return: kw['error'] and kw['error_message'] If there are errors
    '''

    def inner_callback(*args, **kw):
        error_message = []
        #email validation check
        try:
            validate_email(args[0].POST['email'])
        except forms.ValidationError:
            kw['errors'] = True
            error_message.append("Please Insert a Valid Email")
        #username validation check
        if not args[0].POST['username'] or len(args[0].POST['username']) < 6:
            kw['errors'] = True
            error_message.append("Please insert a valid username")
        #check pwd and confirmation
        if not args[0].POST['password'] == args[0].POST['password_repeat'] or len(args[0].POST['password']) < 6:
            kw['errors'] = True
            error_message.append("Password must be equals and with at least 8 characters")
        kw['errors_message'] = error_message
        return callback(*args, **kw)
    return inner_callback


#  **********************************************************
#  *  Routes                                                *
#  **********************************************************

def index(request):
    if request.method == "POST":
        return post(request)
    else:
        return render(request, 'registration/index.html')


@post_validator
def post(request, *args, **kw):

    if kw.get('errors'):
        return render(request, 'registration/index.html', {'errors': kw.get("errors_message"), "values":request.POST})

    return render(request, 'registration/index.html')

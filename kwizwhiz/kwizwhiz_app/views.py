from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import *
import bcrypt

def homepage(request):
    pass

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/logreg')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        print(pw_hash)
        user = User.objects.create(first_name = request.POST['first_name'], 
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = pw_hash)
        messages.success(request, "Registration successful!")
        request.session['id'] = user.id
        request.session['name'] = user.first_name
        return redirect('/selectcategory')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/logreg')
        else:
            user = User.objects.get(email = request.POST['email'])
            request.session['id'] = user.id
            request.session['name'] = user.first_name
            return redirect('/selectcategory')

# def updateaccount(request, user_id):
#     pass

def selectcategory(request):
    pass

def selecttopic(request, category_id):
    pass

def selectquiz(request, topic_id):
    pass

def takequiz(request, quiz_id):
    pass

def processquiz(request, quiz_id):
    pass

def results(request, quiz_id):
    pass

def logout(request):
    request.session.flush()
    return redirect('/')

# Create your views here.

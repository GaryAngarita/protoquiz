from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import *
import bcrypt

def homepage(request):
    return render(request, "homepage.html")

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
    context = {
        "categories": Category.objects.all()
    }
    return render(request, "selectcategory.html", context)

def selecttopic(request, category_id):
    category = Category.objects.get(id = category_id)
    context = {
        "topics": category.topics.all()
    }
    return render(request, "selecttopic.html", context)

def selectquiz(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    quizzes = Quiz.objects.all()
    context = {
        "topic": topic,
        "quizzes": quizzes

    }
    return render(request, "selectquiz.html", context)

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

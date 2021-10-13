from django.shortcuts import render, redirect

def index(request):
    pass

def register(request):
    pass

def login(request):
    pass

def selectcategory(request):
    pass

def selecttopic(request, category_id):
    pass

def selectquiz(request, topic_id):
    pass

def processquiz(request, quiz_id):
    pass

def results(request, quiz_id):
    pass

def logout(request):
    request.session.flush()
    return redirect('/')

# Create your views here.

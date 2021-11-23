from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
import bcrypt

def homepage(request):
    return render(request, "homepage.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def media(request):
    return render(request, "media.html")

def recommend(request):
    return render(request, "recommend.html")
    
def logreg(request):
    return render(request, "logreg.html")

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
        errors = User.objects.log_validator(request.POST)
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
    if 'id' not in request.session:
        return redirect('/')
    else:
        context = {
            "categories": Category.objects.all()
        }
    return render(request, "selectcategory.html", context)

def selecttopic(request, category_id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        category = Category.objects.get(id = category_id)
        request.session['category'] = category.selection
        context = {
            "topics": category.topics.all()
        }
    return render(request, "selecttopic.html", context)

def selectquiz(request, topic_id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        topic = Topic.objects.get(id = topic_id)
        quizzes = Quiz.objects.all()
        context = {
            "topic": topic,
            "quizzes": quizzes

        }
    return render(request, "selectquiz.html", context)

def takequiz(request, quiz_id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        quiz = Quiz.objects.get(id = quiz_id)
        questions = Question.objects.all()
        answers = Answer.objects.all()
        context = {
            "answers": answers,
            "questions": questions,
            "quiz": quiz,
            "quizzes": Quiz.objects.all()
        }
    return render(request, "takequiz.html", context)

def processquiz(request, quiz_id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        if request.method == 'POST':
            quiz = Quiz.objects.get(id = quiz_id)
            context = {
                "quiz": quiz,
            }
            Count.objects.create(count = request.POST['count'])
            count = 0
            total = 0
            wrong = 0
            correct = 0
            score = 0
            average = 0
            for question in quiz.questions.all():
                total += 1
                for answer in question.answers.all():
                    if answer.is_right and answer.answer_text == request.POST['answer-'+str(question.id)]:              
                        correct += 1
                    elif not answer.is_right and answer.answer_text == request.POST['answer-'+str(question.id)]:
                        wrong += 1
            count += 1
            score = round((correct/total) * 100)
            request.session['score'] = score
            Score.objects.create(score = score)
            request.session['correct'] = correct
            request.session['wrong'] = wrong
            request.session['total'] = total
            average = round(round(score + request.session['score']) / count)
            request.session['average'] = average
    
            return redirect(f'/results/{quiz.id}', context)
        else:
            return redirect('/')

def results(request, quiz_id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        context = {
            "quiz": Quiz.objects.get(id = quiz_id)
        }
    return render(request, "results.html", context)

def dashboard(request):
    if 'id' not in request.session:
        return redirect('/')
    else:
        quiz = request.session['quiz']
        context = {
            "quiz": quiz,
        }    
    return render(request, "dashboard.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')

# Create your views here.

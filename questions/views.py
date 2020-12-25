from django.shortcuts import render, redirect
from django.template import loader
from .models import Question
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth import authenticate, login, logout


def index(request):
    questions = Question.objects.all()
    content = {'questions': questions}
    return render(request, "questions/index.html", content)


def dictfetchall(cursor): #for search results
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def search_view(request):
    if 'query' in request.GET:
        content = {}
        search = request.GET['query']
        query = "SELECT id,title FROM questions_question WHERE title like '%%" +search+"%%' or content like '%%"+search+"%%'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = dictfetchall(cursor)
            content = {'results': rows}
        return render(request, "questions/search.html", content)
    return render(request, "questions/search.html")


def reservation_view(request):
    questions = Question.objects.all()
    content = {'questions': questions}
    return render(request, "questions/reserve_question.html", content)


def reserve_question(request, question_id, user_id):
    question = Question.objects.get(pk=question_id)
    user = User.objects.get(username=user_id)
    question.assignee = user
    question.save()
    return redirect("/questions/reserve")


def edit_answer_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.POST:
        print(request.POST['content'])
        question.content = request.POST['content']
        question.save()
        return redirect('/questions/view/'+str(question_id))
    content = {'entry': question}
    return render(request, "questions/add_answer.html", content)


def answer_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    content = {'entry': question}
    return render(request, "questions/view_answer.html", content)


def login_view(request):
    user = None
    if 'username' in request.POST:
        if 'password' in request.POST:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/questions')
    else:
        return render(request, "questions/login.html")


def logout_view(request):
    logout(request)
    return redirect('/questions')

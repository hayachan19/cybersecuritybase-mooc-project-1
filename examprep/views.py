from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>2020 BIG Exam Prep Website</h1><a href='/questions'>Questions and Answers</a>")
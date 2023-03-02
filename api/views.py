from django.http import HttpResponse

def index(request):
    return  HttpResponse("WELCOME TO THE WORLD")
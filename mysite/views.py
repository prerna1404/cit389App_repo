from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello World! Hello from Elastic Beanstalk Django App!")

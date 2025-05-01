from django.http import HttpResponse
def home(request):
    return HttpResponse("Atlantis University! Hello from Elastic Beanstalk Django App!")

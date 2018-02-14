from django.shortcuts import render

def index(request):
   return render(request, 'cam2intro/home.html')
# Create your views here

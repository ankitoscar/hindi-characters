from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'uploader/homepage.html')

def upload(request):
    return render(request, 'uploader/main.html')

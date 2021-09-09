from django.shortcuts import render
from .forms import ImageForm


# Create your views here.

def index(request):
    return render(request, 'uploader/homepage.html')

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            return render(request, 'uploader/main.html', {'form': form, 'img_obj': img_obj})

    else:
        form = ImageForm()
    return render(request, 'uploader/main.html', {'form': form})

from django.shortcuts import render
from django.conf import settings
from numpy.core.defchararray import equal
from .forms import ImageForm
import tensorflow as tf
from tensorflow import keras
import h5py
import numpy as np
import cv2


global result, model 
model = tf.keras.models.load_model(settings.MODEL_PATH)
print("Model loaded!!!")
# Create your views here.

def index(request):
    return render(request, 'uploader/homepage.html')

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            img = cv2.imread((img_obj.image.path))
            img1 = np.zeros((64, 64, 3))
            equal_array = np.equal(img, img1)
            equal_array = equal_array.astype('float32')
            grayscale = cv2.cvtColor(equal_array, cv2.COLOR_BGR2GRAY)
            print(grayscale.shape)
            global result
            grayscale = np.expand_dims(grayscale, axis=[0, 3])
            print(grayscale.shape)
            result = np.argmax(model.predict(grayscale))

            return render(request, 'uploader/main.html', {'form': form, 'img_obj': img_obj})

    else:
        form = ImageForm()
    return render(request, 'uploader/main.html', {'form': form})

def result(request):
    return render(request, 'uploader/result.html', {'result': result})


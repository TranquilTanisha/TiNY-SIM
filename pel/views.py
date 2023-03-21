#import required libs and files
from django.shortcuts import render, redirect
from . models import Encode, Decode
from . forms import EncodeForm, DecodeForm
from .utils import hideData, decode_text

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import cv2
import os
import numpy as np

# Create your views here.

def home(request):
    return render(request, "pel/home-copy.html")

#function for encoding the information
def encode(request):
    form=EncodeForm()
    if request.method=="POST":
        form=EncodeForm(request.POST, request.FILES)
        if form.is_valid():
            
            encode=form.save(commit=False)
            image=form.cleaned_data.get("image") #get the image uploaded by user
            message=form.cleaned_data.get("message") #get the information to encode
            filename=form.cleaned_data.get("filename") #get the filename of the output image
            
            encode.image = image
            encode.message = message
            uploaded_file_name = image.name #get the name of the imput image
            encode.save()
            uploaded_file_name = './static/images/encoded/' + uploaded_file_name #to get the location of imput image
            
            img = cv2.imread(uploaded_file_name)
            encoded_image = hideData(img, message)
            success, encoded_image = cv2.imencode('.png',encoded_image) #to convert the output of hideData and pseudo-load the image
            encode_image_bytes = encoded_image.tobytes() #convert the pseudo-loaded image into bytes 
            # data=encode.image.read() ##Alternative

            response=HttpResponse(encode_image_bytes, content_type='application/png')
            response["Content-Disposition"]="attachment; filename=%s.png " % encode.filename
            return response
        
    contxt={"form":form}
    return render(request, "pel/encode.html", contxt)

def download(request, pk):
    encode=Encode.objects.get(id=pk)
    return render(request, "pel/download.html", {"encode":encode})

def decode(request):
    form=DecodeForm()
    if request.method=="POST":
        form=DecodeForm(request.POST, request.FILES)
        if form.is_valid():
            decode=form.save(commit=False)

            image=form.cleaned_data.get("image")
            decode.image=image
            txt=decode_text(image)
            #txt="abc"
            decode.message=txt
            decode.save()
            return render(request, "pel/result-decode.html", {"decode":decode})

    return render(request, "pel/decode.html", {"form":form})

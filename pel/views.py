from django.shortcuts import render, redirect
from . models import Encode, Decode
from . forms import EncodeForm, DecodeForm
from .utils import hideData, decode_text
from . password import generate_password
from django.contrib import messages

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import cv2
import numpy as np

# Create your views here.

def home(request):
    return render(request, "pel/home-copy.html")

def about(request):
    return render(request, "pel/about.html")

#function for encoding the information
def encode(request):
    form=EncodeForm()
    context={}
    if request.method=="POST":
        form=EncodeForm(request.POST, request.FILES)

        if form.is_valid():            
            encode=form.save(commit=False)
            # image=form.cleaned_data.get("image") #get the image uploaded by user
            # message=form.cleaned_data.get("message") #get the information to encode
            # filename=form.cleaned_data.get("filename") #get the filename of the output image

            image=encode.image
            message=encode.message
            
            # encode.image = image
            # encode.message = message
            
            img_bytes = image.file.read()
            uploaded_array = np.frombuffer(img_bytes, np.uint8)
            uploaded_file = cv2.imdecode(uploaded_array,cv2.IMREAD_COLOR) #to convert the output of hideData and pseudo-load the image
            encoded_image,key = hideData(uploaded_file, message)
            success, encoded_image = cv2.imencode('.png',encoded_image) #to convert the output of hideData and pseudo-load the image
            encode_image_bytes = encoded_image.tobytes() #convert the pseudo-loaded image into bytes 
            # data=encode.image.read() ##Alternative

            print(key)

            key=key[3:-1]
            #print(key)
            #print(key[0])
            key=key.split("'")
            #print(key)
            k=key[3]
            for i in range(7,len(key),4):
                k+=key[i]

            print(k)

            messages.info(request, "Your key is: ")
            
            response=HttpResponse(encode_image_bytes, content_type='application/png')
            response["Content-Disposition"]="attachment; filename=%s.png " % encode.filename
            return response
        
    context['form']=form
    return render(request, "pel/encode.html", context)

def download(request, pk):
    encode=Encode.objects.get(id=pk)
    return render(request, "pel/download.html", {"encode":encode})

def decode(request):
    form=DecodeForm()

    if request.method=="POST":
        form=DecodeForm(request.POST, request.FILES)

        if form.is_valid():
            decode=form.save(commit=False)

            # image=form.cleaned_data.get("image")
            # key=form.cleaned_data.get("key")
            # decode.image=image
            # decode.key=key

            image=decode.image
            key=decode.key

            img_bytes = image.file.read()
            uploaded_array = np.frombuffer(img_bytes, np.uint8)
            uploaded_file = cv2.imdecode(uploaded_array,cv2.IMREAD_COLOR)

            txt=decode_text(uploaded_file,key)
            #txt="abc"
            decode.message=txt
            decode.save()
            return render(request, "pel/result-decode.html", {"decode":decode})

    return render(request, "pel/decode.html", {"form":form})
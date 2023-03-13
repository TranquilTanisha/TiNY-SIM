from django.shortcuts import render, redirect
from . models import Encode, Decode
from . forms import EncodeForm, DecodeForm
from .utils import hideData, decode_text

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def home(request):
    return render(request, "pel/home-copy.html")

def encode(request):
    form=EncodeForm()
    if request.method=="POST":
        form=EncodeForm(request.POST, request.FILES)
        if form.is_valid():
            encode=form.save(commit=False)

            image=form.cleaned_data.get("image")
            message=form.cleaned_data.get("message")
            encoded_image = hideData(image, message)
            #encoded_image = form.cleaned_data.get("image")
            encode.image=encoded_image
            encode.save()

            data=encode.image.read()

            response=HttpResponse(data, content_type='application/png')
            response["Content-Disposition"]="attachment; filename=%s.jpg " % encode.filename
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
            #text="abc"
            decode.message=txt
            decode.save()
            return render(request, "pel/result-decode.html", {"decode":decode})

    return render(request, "pel/decode.html", {"form":form})

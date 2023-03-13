from django.shortcuts import render, redirect
from . models import Encode, Decode
from . forms import EncodeForm, DecodeForm
#from .utils import hideData, messageToBinary

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

            '''image=form.cleaned_data.get("image")
            message=form.cleaned_data.get("message")
            encoded_image = hideData(image, message)'''
            filename=form.cleaned_data.get("filename")
            encoded_image = form.cleaned_data.get("image")
            encode.image=encoded_image
            encode.save()

            '''context={"encode":encode}

            template_path="pel/download.html"
            response=HttpResponse(content_type='application/pdf')
            response["Content-Disposition"]="attachment; filename=%s.pdf " % encode.filename
            template=get_template(template_path)
            html=template.render(context)

            pisa_status=pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse("We had some errors <pre>"+html+"</pre>")
            return response'''

            return render(request, "pel/download.html", {"encode":encode, "form": form})
        
    contxt={"form":form}
    return render(request, "pel/encode.html", contxt)

def encodingresult(request, pk):
    encode=Encode.objects.get(id=pk)
    return render(request, "pel/result-encode.html", {"image":encode.image, "id":pk})

'''def download(request, pk):
    encode=Encode.objects.get(id=pk)
    context={"encode":encode}

    template_path="pel/download.html"
    response=HttpResponse(content_type='application/png')
    response["Content-Disposition"]="attachment; filename=%s.png " % encode.filename
    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>"+html+"</pre>")
    return response'''

def download(request, pk):
    encode=Encode.objects.get(id=pk)
    return render(request, "pel/download.html", {"image":encode.image, "id":pk})


def decode(request):
    form=DecodeForm()
    return render(request, "pel/decode.html", {"form":form})

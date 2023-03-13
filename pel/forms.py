from django.forms import ModelForm
from django import forms
from . models import Encode, Decode

class EncodeForm(ModelForm):
    class Meta:
        model = Encode
        fields = ['image', 'filename', 'message']
        widgets = {
            'image': forms.FileInput(attrs={'id': 'uploadedimgcontainer'}),
            'message': forms.TextInput(attrs={'id': 'message'}),
            'filename': forms.TextInput(attrs={'id': 'filename'}),
        }
        labels = {
            "image": "",
            "message": "",
            "filename": "",
        }

    def __init__(self, *args, **kwargs):
        super(EncodeForm,self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({"class": "input", "placeholder": "Add an image"})
        self.fields['message'].widget.attrs.update({"class": "input", "placeholder": "Add a message to be encoded in the image"})
        self.fields['filename'].widget.attrs.update({"class": "input", "placeholder": "New filename"})

class DecodeForm(ModelForm):
    class Meta:
        model = Decode
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'id': 'uploadedimgcontainer'}),
            #'message': forms.TextInput(attrs={'id': 'message'}),
        }
        labels = {
            "image": "",
            #"message": ""
        }

    def __init__(self, *args, **kwargs):
        super(DecodeForm,self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({"class": "input", "placeholder": "Add an image"})
        #self.fields['message'].widget.attrs.update({"class": "input", "placeholder": "Add a message to be encoded in the image"})
       
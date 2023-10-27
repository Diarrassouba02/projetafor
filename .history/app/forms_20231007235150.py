from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'

class TranscriptionForm(forms.Form):
    transcription = forms.CharField(widget=forms.Textarea(attrs={'class': 'transcription-textarea'}))

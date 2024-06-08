from django import forms
from . models import *

class NotesForms(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']
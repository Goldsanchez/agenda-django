from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Agenda


class AgendaForm(ModelForm):
    
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {'creador': forms.TextInput(attrs={'value': '', 'id':'name', 'type': 'hidden'})}
from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
import datetime
from django.core.files.storage import default_storage

class TopForms(forms.Form):
    type = forms.ChoiceField()
    image = forms.ImageField()

    
    
import logging
from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
import datetime
from django.core.files.storage import default_storage

logger = logging.getLogger(__name__)

class ReaderForm(forms.Form):
    license_type = forms.ChoiceField(
        choices=(
            ('license1', '保険証'),
            ('license2', '運転免許証'),
            ('license3', '電気工事士資格証')
        ),
        required=True
    
    def analyze(self):
        logger.info(self.cleaned_data['license_type'])

    file = forms.ImageField(label='読込画像の選択')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)

    


    
    
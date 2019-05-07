
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from signage.templates.models import Template


class TemplateChangeForm(ModelForm):

    class Meta:
        model = Template
        fields = ['name', 'template', 'background']


class TemplateCreationForm(ModelForm):

    class Meta:
        model = Template
        fields = ['name', 'template', 'background']



from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from signage.screens.models import Screen


class ScreenChangeForm(ModelForm):
    class Meta:
        model = Screen
        fields = ['name', 'menu', 'is_external']


class ScreenCreationForm(ModelForm):

    class Meta:
        model = Screen
        fields = ['name', 'menu', 'is_external']


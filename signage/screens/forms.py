
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from signage.screens.models import Screen
from signage.menus.models import Menu


class ScreenChangeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScreenChangeForm, self).__init__(*args, **kwargs)
        self.fields['menu'].choices = [(o.id, o.name) for o in Menu.objects.all()]

    class Meta:
        model = Screen
        fields = ['name', 'menu', 'is_external', 'is_vertical']


class ScreenCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ScreenCreationForm, self).__init__(*args, **kwargs)
        self.fields['menu'].choices = [(o.id, o.name) for o in Menu.objects.all()]

    class Meta:
        model = Screen
        fields = ['name', 'menu', 'is_external', 'is_vertical']


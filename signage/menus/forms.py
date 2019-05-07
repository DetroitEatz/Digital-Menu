
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from signage.menus.models import Menu, Item


class MenuChangeForm(ModelForm):

    class Meta:
        model = Menu
        fields = ['name', 'template']


class MenuCreationForm(ModelForm):

    class Meta:
        model = Menu
        fields = ['name', 'template']


class ItemChangeForm(ModelForm):

    class Meta:
        model = Item
        fields = ["identifier", "name", "image", "status", "has_status", "menu"] #"description", "price",


class ItemCreationForm(ModelForm):

    class Meta:
        model = Item
        fields = ["identifier", "name", "image", "status", "has_status", "menu"] #"description", "price",






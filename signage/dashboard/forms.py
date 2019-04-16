
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from signage.menus.models import Item


class DashboardChangeForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'status']


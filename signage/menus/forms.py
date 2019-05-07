
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from signage.menus.models import Menu, Slot
from signage.templates.models import Template


class MenuChangeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MenuChangeForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices = [(o.id, o.name) for o in Template.objects.all()]

    class Meta:
        model = Menu
        fields = ['name', 'template', 'background']


class MenuCreationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MenuCreationForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices = [(o.id, o.name) for o in Template.objects.all()]

    class Meta:
        model = Menu
        fields = ['name', 'template', 'background']


class SlotChangeForm(ModelForm):
    # status --> 1 = good, 2 = running low 3 = I'm out

    def __init__(self, *args, **kwargs):
        super(SlotChangeForm, self).__init__(*args, **kwargs)
        self.fields['menu'].choices = [(o.id, o.name) for o in Menu.objects.all()]


    class Meta:
        model = Slot
        fields = ["name", "image", "status", "menu"]


class SlotCreationForm(ModelForm):
    #status --> 1 = good, 2 = running low 3 = I'm out

    def __init__(self, *args, **kwargs):
        super(SlotCreationForm, self).__init__(*args, **kwargs)
        self.fields['menu'].choices = [(o.id, o.name) for o in Menu.objects.all()]

    class Meta:
        model = Slot
        fields = ["name", "image", "status", "menu"]





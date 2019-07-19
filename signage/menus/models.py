from django.db import models
from signage.contrib.models import BaseModel
from signage.templates.models import Template
from django.core.validators import MaxValueValidator, MinValueValidator


class Menu(BaseModel):
    """
    A menu represents the content to be displayed on a physical Screen. It has a template and may have a background image.
    """
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "menus"

    name = models.CharField(max_length=255, null=False, blank=False)
    template = models.ForeignKey(Template, null=True, on_delete=models.SET_NULL)
    #template = models.FileField(upload_to='menus/templates/', null=True, blank=True)
    background = models.FileField(upload_to='menus/backgrounds/', null=True, blank=True)


class Slot(BaseModel):
    """
    A Slot represents a part of a Menu in which we want to have a visible status indicator. It can also have an image.
    """
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "menu_slots"

    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.FileField(upload_to='menus/images/', null=True, blank=True)
    status = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(4), MinValueValidator(1)]) # 1 = good, 2 = running low 3 = I'm out, 4 = Other
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)

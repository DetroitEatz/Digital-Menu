from django.db import models
from signage.contrib.models import BaseModel


class Menu(BaseModel):
    class Meta:
        db_table = "menus"

    name = models.CharField(max_length=255, null=True)
    template = models.FileField(upload_to='menus/', null=True, blank=True)
    background = models.FileField(upload_to='backgrounds/', null=True, blank=True)


class Item(BaseModel):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "menu_items"

    identifier = models.TextField(null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.TextField(null=True)
    image = models.FileField(upload_to='images/', null=True)
    status = models.PositiveSmallIntegerField()
    has_status = models.BooleanField(default=False)
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
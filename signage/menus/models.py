from django.db import models
from signage.contrib.models import BaseModel


class Menu(BaseModel):
    class Meta:
        db_table = "menus"

    name = models.CharField(max_length=255, null=True)
    template = models.FileField(upload_to='templates/menus/', null=True)
    background = models.FileField(upload_to='templates/backgrounds/', null=True)


class Item(BaseModel):
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "menu_items"

    identifier = models.TextField(null=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.TextField(null=True)
    image = models.FileField(upload_to='media/', null=True)
    status = models.PositiveSmallIntegerField()
    has_status = models.BooleanField(default=False)
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
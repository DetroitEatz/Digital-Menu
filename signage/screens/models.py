from django.db import models
from signage.contrib.models import BaseModel
from signage.menus.models import Menu


class Screen(BaseModel):

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "screens"

    name = models.CharField(max_length=100, null=True)
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.SET_NULL)
    is_external = models.BooleanField(default=True)
    is_vertical = models.BooleanField(default=True)


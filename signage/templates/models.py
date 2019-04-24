from django.db import models
from signage.contrib.models import BaseModel


class Template(BaseModel):
    class Meta:
        db_table = "templates"

    name = models.CharField(max_length=255, null=True)
    template_file = models.TextField(null=True, blank=True)
    background = models.FileField(upload_to='templates/backgrounds/', null=True, blank=True)


class Slot(BaseModel):
    class Meta:
        db_table = "slots"

    name = models.CharField(max_length=255, null=True)
    template_file = models.TextField(null=True, blank=True)
    background = models.FileField(upload_to='templates/backgrounds/', null=True, blank=True)


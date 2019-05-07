from django.db import models
from signage.contrib.models import BaseModel


class Template(BaseModel):
    """
    A Template represents the visual layout that will be used by a Menu. It is the link to an actual html page.
    """

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "templates"

    name = models.CharField(max_length=255, null=True)
    template = models.FileField(upload_to='templates/', null=True, blank=True)


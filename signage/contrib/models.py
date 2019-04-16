from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

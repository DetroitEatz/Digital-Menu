from django.db import models
from signage.contrib.models import BaseModel
from signage.menus.models import Menu


class Screen(BaseModel):
    """
    A Screen represents a physical display. For future reference, we've included boolean fields
    for whether a display is inside or outside the building and whether it is orientated vertically.

    The associated Menu is what will be displayed on the screen.
    """

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "screens"

    name = models.CharField(max_length=100, null=False, blank=False)
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.SET_NULL)
    is_external = models.BooleanField(default=True)
    is_vertical = models.BooleanField(default=True)


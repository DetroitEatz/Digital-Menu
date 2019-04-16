from django.contrib import admin
from signage.screens.models import Screen

from signage.screens.forms import ScreenChangeForm, ScreenCreationForm


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):

    form = ScreenChangeForm
    add_form = ScreenCreationForm
    #fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["name"]
    search_fields = ["name"]

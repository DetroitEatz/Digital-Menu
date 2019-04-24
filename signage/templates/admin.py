from django.contrib import admin

from signage.templates.models import Template

from signage.templates.forms import TemplateChangeForm, TemplateCreationForm, ItemChangeForm, ItemCreationForm


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):

    form = TemplateChangeForm
    add_form = TemplateCreationForm
    #fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    form = ItemChangeForm
    add_form = ItemCreationForm
    #fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["name"]
    search_fields = ["name"]



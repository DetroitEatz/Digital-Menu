from django.contrib import admin

from signage.templates.models import Template

from signage.templates.forms import TemplateChangeForm, TemplateCreationForm


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):

    form = TemplateChangeForm
    add_form = TemplateCreationForm
    #fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["name"]
    search_fields = ["name"]

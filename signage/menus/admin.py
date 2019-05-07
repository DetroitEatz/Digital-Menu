from django.contrib import admin

from signage.menus.models import Menu, Slot

from signage.menus.forms import MenuChangeForm, MenuCreationForm, SlotChangeForm, SlotCreationForm


class CSSAdminMixin():
    """
    This is a one-time mclass used to override the overall admin css
    """
    class Media:
        css = {
            'all': ('css/admin.css',),
        }

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin, CSSAdminMixin):

    form = MenuChangeForm
    add_form = MenuCreationForm
    #fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):

    form = SlotChangeForm
    add_form = SlotCreationForm
    #fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["name"]
    search_fields = ["name"]



from django.contrib import admin

from signage.menus.models import Menu, Item

from signage.menus.forms import MenuChangeForm, MenuCreationForm, ItemChangeForm, ItemCreationForm


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    form = MenuChangeForm
    add_form = MenuCreationForm
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

from django.urls import path

from signage.menus.views import (
    Menu_list_view,
    Menu_update_view,
    Menu_detail_view,
)

app_name = "menus"
urlpatterns = [
    path("", view=Menu_list_view, name="list"),
    path("~update/(?P<pk>[\w-]+)$", view=Menu_update_view, name="update"),
    path("<id>/", view=Menu_detail_view, name="detail"),
]

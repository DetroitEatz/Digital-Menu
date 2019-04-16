from django.urls import path

from signage.screens.views import (
    Screen_list_view,
    Screen_redirect_view,
    Screen_update_view,
    Screen_detail_view,
)

app_name = "screens"
urlpatterns = [
    path("", view=Screen_list_view, name="list"),
    path("~redirect/", view=Screen_redirect_view, name="redirect"),
    path("~update/", view=Screen_update_view, name="update"),
    path("<id>/", view=Screen_detail_view, name="detail"),
]

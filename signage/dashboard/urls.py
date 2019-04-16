from django.urls import path

from signage.dashboard.views import Dashboard_list_view

app_name = "dashboard"
urlpatterns = [
    path("", view=Dashboard_list_view, name="list"),
]
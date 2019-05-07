
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from signage.menus.models import Slot


class DashboardListView(ListView):

    model = Slot
    slug_field = "name"
    slug_url_kwarg = "name"


Dashboard_list_view = DashboardListView.as_view()


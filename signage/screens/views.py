
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from signage.screens.models import Screen


class ScreenDetailView(DetailView):

    model = Screen
    slug_field = "name"
    slug_url_kwarg = "name"


Screen_detail_view = ScreenDetailView.as_view()


class ScreenListView(ListView):

    model = Screen
    slug_field = "name"
    slug_url_kwarg = "name"


Screen_list_view = ScreenListView.as_view()


class ScreenUpdateView(UpdateView):

    model = Screen
    fields = ["name"]

    def get_success_url(self):
        return reverse("Screens:detail", kwargs={"name": self.request.Screen.name})

    def get_object(self):
        return Screen.objects.get(Screenname=self.request.Screen.Screenname)


Screen_update_view = ScreenUpdateView.as_view()


class ScreenRedirectView(RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("Screens:detail", kwargs={"name": self.request.Screen.name})


Screen_redirect_view = ScreenRedirectView.as_view()

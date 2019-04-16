
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from signage.menus.models import Menu
from signage.menus.models import Item


def menu_view(request, id):
    print("menu_view")
    menu = get_object_or_404(Menu, pk=id)

    if menu.template and menu.background:
        items = Item.objects.all().filter(pk=id)
        return render(request, menu.template.url.replace('/media/', ""), context={'background': menu.background, 'items': items})

    template = "menus/default.html"
    if menu.background:
        print("show default")
        return render(request, template, context={'background': menu.background})


class MenuDetailView(DetailView):

    model = Menu
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_success_url(self):
        return reverse("Menus:detail", kwargs={"id": self.request.Menu.id})

    def get_object(self):
        return Menu.objects.get(id=self.kwargs['id'])


Menu_detail_view = MenuDetailView.as_view()


class MenuListView(ListView):

    model = Menu
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_queryset(self):
        qs = super(MenuListView, self).get_queryset()
        qs = qs.filter(has_status=True)
        return qs


Menu_list_view = MenuListView.as_view()


class MenuUpdateView(UpdateView):

    model = Menu
    fields = ["id","name"]

    def get_success_url(self):
        return reverse("Menus:detail", kwargs={"id": self.request.Menu.id})

    def get_object(self):
        return Menu.objects.get(id=self.kwargs['id'])


Menu_update_view = MenuUpdateView.as_view()


class MenuRedirectView(RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("Menus:detail", kwargs={"name": self.request.Menu.name})


Menu_redirect_view = MenuRedirectView.as_view()


class ItemDetailView(DetailView):

    model = Item
    slug_field = "name"
    slug_url_kwarg = "name"


Item_detail_view = ItemDetailView.as_view()


class ItemListView(ListView):

    model = Item
    slug_field = "name"
    slug_url_kwarg = "name"


Item_list_view = ItemListView.as_view()


class ItemUpdateView(UpdateView):

    model = Item
    fields = ["name"]

    def get_success_url(self):
        return reverse("Menus:detail", kwargs={"name": self.request.Menu.Menuname})

    def get_object(self):
        return Item.objects.get(name=self.request.Item.name)


Item_update_view = ItemUpdateView.as_view()


class ItemRedirectView(RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("Menus:detail", kwargs={"name": self.request.Item.name})


Item_redirect_view = ItemRedirectView.as_view()

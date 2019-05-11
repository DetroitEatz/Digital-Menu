
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views import View

from django.views.decorators.csrf import csrf_exempt

from signage.menus.models import Menu, Slot


class DashboardListView(ListView):

    model = Menu
    slug_field = "name"
    slug_url_kwarg = "name"

    context_object_name = 'menus'
    slots =  Slot.objects.order_by('menu').values_list('menu', flat=True)
    queryset = Menu.objects.filter(id__in=slots).all()
    template_name = 'dashboard.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['slots'] = Slot.objects.order_by('menu').all()
        return context


Dashboard_list_view = DashboardListView.as_view()

@csrf_exempt
def status_view(request, *args, **kwargs):
    slot_id = request.POST.get('slot')
    status = request.POST.get('status')

    slot = Slot.objects.get(pk=slot_id)
    slot.status = status
    slot.save()

    return HttpResponse()

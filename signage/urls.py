"""menus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from signage.dashboard.views import Dashboard_list_view
from signage.menus.views import menu_view


admin.site.site_header = 'Detroit Eats Menu Administration'                    # default: "Django Administration"
admin.site.index_title = 'Detroit Eats'                 # default: "Site administration"
admin.site.site_title = 'Detroit Eats Menu Administration' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/<id>/', view=menu_view, name="menu_display"),
    path('menus/', include("signage.menus.urls")),
    path("", view=Dashboard_list_view, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

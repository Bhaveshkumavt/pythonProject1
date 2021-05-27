from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from . import settings


# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('', RedirectView.as_view(url='app1')),
    path('accounts/', include('registration.backends.default.urls')),
    path('account/', include('allauth.urls')),         #from ecom

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

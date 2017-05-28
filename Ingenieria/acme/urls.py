
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
  url(r'^$', views.indexNotRegister, name='index'),
  url(r'^signup-successful/$', views.register, name='Register'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^signup-Client/$', views.signupClient, name='signupCliente'),
  url(r'^signup-Vendedor-Fijo/$', views.signupVendFijo, name='signupFijo'),
  url(r'^signup-Vendedor-Ambulante/$', views.signupVendAmb, name='signupAmb'),
  url(r'^gestion/', views.gestion, name='gestion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

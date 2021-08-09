from django.conf.urls import url
from apiapp import views

urlpatterns = [
    url(r'^api/apiapp$', views.countries_list),
    url(r'^api/apiapp/(?P<pk>[0-9]+)$', views.countries_details)
   



]
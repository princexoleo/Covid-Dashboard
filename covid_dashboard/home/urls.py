from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
     path("", views.index, name="home"),
     url('selectCountry',views.drillDownACountry,name='drillDown'),
]

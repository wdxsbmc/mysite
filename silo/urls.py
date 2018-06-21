from django.urls import path

from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#
#]


from django.conf.urls import url,include
from django.contrib import admin
import silo.views
admin.autodiscover()

urlpatterns = [
        url(r'^index/$',views.index),
        url(r'^login/$',views.login),
        url(r'^regist/$',views.regist),


]

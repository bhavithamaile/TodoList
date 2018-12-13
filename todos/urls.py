from django.conf.urls import url
from . import views

urlpatterns = [
  url('home',views.index, name='index'),
  url('details/(?P<id>\w{0,50})', views.details),
  url('add',views.add,name='add'),
]
from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [



# list view



url(r'^$',views.index, name='contentdetail'),

url(r'^new/$',views.indexs, name='content'),




]

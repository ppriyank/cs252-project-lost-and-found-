
from django.conf.urls import url
from . import views

urlpatterns = [

    #/database
    url(r'^$', views.index, name='index' ),
    url(r'^viewdatabase/', views.form),
    #/database/id_details
    url(r'^(?P<data_id>[0-9]+)/$', views.Details , name='details' ),
    url(r'^form/$', views.form, name='index'),
]

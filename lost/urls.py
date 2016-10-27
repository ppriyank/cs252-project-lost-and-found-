
from django.conf.urls import url
from . import views

urlpatterns = [

    #/database
    url(r'^$', views.index, name='index' ),
    # url(r'^viewdatabase/', admin.site.urls),
    #/database/id_details
    url(r'^(?P<data_id>[0-9]+)/$', views.Details , name='details' ),
]

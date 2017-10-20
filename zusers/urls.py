from django.conf.urls import url

from zusers.views import *

urlpatterns = [
    url(r'^$', zusers_index, name = "zusers_index"),
    url(r'^login', zusers_login, name = "login"),
] 
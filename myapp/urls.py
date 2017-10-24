from django.conf.urls import url

from myapp.views import *

urlpatterns = [
    # url(r'^$', index),
    # url(r'^sampletable/', sampletable),
    url(r'^deploy/', deploy, name = "deploy"),
    # url(r'^alist/', alist, name = "alist"),
    # url(r'^ajax_list/', ajax_list, name = "ajax_list"),
    url(r'^ajax_deploy/', ajax_deploy, name = "ajax_deploy"),
    url(r'^ajax_rollback/', ajax_rollback, name = "ajax_rollback"),
    # url(r'^upload_test/', simple_upload, name = "upload_test"),
    url(r'^ajax_test/', ajax_test, name = "ajax_test"),
] 
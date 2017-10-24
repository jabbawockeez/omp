# coding: utf-8

from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.http import HttpResponse
from .forms import *
import json
from django.core.files.storage import FileSystemStorage
from .deploymanager import *
from .package import *


# Create your views here.

# def index(request):

    # method 1
    # return render_to_response("myapp/index.html")

    # method 2
    # return render(request, "myapp/index.html")


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render_to_response('myapp/upload_test.html', {'uploaded_file_url': uploaded_file_url})

#     return render_to_response("myapp/upload_test.html")


def deploy(request):

    # print(request)

    request.breadcrumbs = [(u"发布变更", reverse("deploy"))]

    form = DeployForm()

    print locals()
    return render(request, "myapp/deploy.html", locals())


def ajax_deploy(request):

    dm = DeployManager(request)

    try:
        dm.deploy()
    except Exception as e:
        return HttpResponse(e)
    else:
        return HttpResponse('deploy success')

def ajax_rollback(request):

    dm = DeployManager(request)

    try:
        dm.rollback()
    except Exception as e:
        return HttpResponse(e)
    else:
        return HttpResponse('rollback success')

def ajax_test(request):

    if request.method == "POST":
        f = DeployForm(request.POST)

        if f.is_valid():
            print f.cleaned_data
            return HttpResponse("yes")
        else:
            print(type(f.errors), f.errors)  #errors类型是ErrorDict，里面是ul，li标签
            return render(request,"myapp/ajax_test.html", {"error" : f.errors})

    else:
        f = DeployForm()

    return render(request, "myapp/ajax_test.html", {'form' : f})
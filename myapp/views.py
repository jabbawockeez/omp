# coding: utf-8

from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.http import HttpResponse
import json
from django.core.files.storage import FileSystemStorage
from .deploymanager import *
from .package import *


# Create your views here.

def index(request):

    # method 1
    # return render_to_response("myapp/index.html")

    # method 2
    return render(request, "myapp/index.html")


# def sampletable(request):
#     return render(request, "myapp/sampletable.html")



# def alist(request):
#     return render_to_response("myapp/ajax_test.html")


# def ajax_list(request):

#     dir(request)
#     print(request.FILES)


#     l = {"a" : 'fhj', 'b' : 2, 'al' : 'hello'}
#     return HttpResponse(json.dumps(l), content_type='application/json')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render_to_response('myapp/upload_test.html', {'uploaded_file_url': uploaded_file_url})

    return render_to_response("myapp/upload_test.html")


def deploy(request):

    # print(request)

    request.breadcrumbs = [(u"发布变更", reverse("deploy"))]

    return render(request, "myapp/deploy.html")


def ajax_deploy(request):

    # print(request.POST.get("server_ip").split(';'))
    # request.package_type = []
    # if 'jar' in request.POST:
    #     request.package_type.append('jar')
    # if 'war' in request.POST: 
    #     request.package_type.append('war')

    # # print(request.package_type)

    # dm = DeployManager(request)

    # try:
    #     # dm.test()
    #     dm.backup_old()
    #     dm.upload()
    #     dm.replace()
    #     dm.restart()
    # except Exception as e:
    #     return HttpResponse(e)
    # else:
    #     return HttpResponse('download success')

    # print request.POST.get('jar_server_ip', "abc")
    # print request.POST['cwar_server_ip']

    # if 'jar' in request.POST:
    #     jdm = JarDeployManager(request)
    # if 'war' in request.POST: 
    #     wdm = WarDeployManager(request)

    # jdm = JarDeployManager(request)
    dm = DeployManager(request)

    try:
        dm.deploy()
    except Exception as e:
        return HttpResponse(e)
    else:
        return HttpResponse('deploy success')

    # JARPackage("abc.txt")

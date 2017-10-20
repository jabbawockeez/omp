# coding: utf-8
from django.shortcuts import render, render_to_response
from django.urls import reverse

def index(request):

    request.breadcrumbs = [(u"首页", reverse("index"))]

    # method 1
    # return render_to_response("myapp/index.html")

    # method 2
    return render(request, "index.html")
# coding: utf-8
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
import time

# Create your views here.

# django.contrib.auth.decorators.login_required([redirect_field_name=REDIRECT_FIELD_NAME,login_url=None])
# 1、redirect_field_name:默认值是next。用来定义登陆成功之后的跳回之前访问界面的url。
# 2、login_url:默认值是settings.LOGIN_URL。用来指定登陆界面的url。如果不传入改参数，就需要确保settings.LOGIN_URL的值是正确设置的。

@login_required
def zusers_index(request):

    request.breadcrumbs = [(u"用户管理", reverse("zusers_index"))]

    # print(request.user)

    print(request.session.session_key)

    request.session.flush()

    return render(request, "zusers/zusers_index.html")


def zusers_login(request):


    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username = uname, password = pwd)

        if user and user.is_active:
            login(request, user)
            # 更新最后登录时间
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user.last_login = now_time
            user.save()
            
            print(request.POST.get("next"))
            return HttpResponseRedirect(request.POST.get("next", '/'))
        else:
            return render(request, 'zusers/login.html',{
                'user_name': uname,
                'user_pwd': pwd,
            })
    else:
        return render(request, "zusers/login.html")
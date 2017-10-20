# coding: utf-8

from django.urls import reverse


def breadcrumbs(request):

    # print(request.breadcrumbs)

    # if request.breadcrumbs[0][0] != u"首页":
    #     request.breadcrumbs.insert(0, (u"首页", "/"))

    if hasattr(request, 'breadcrumbs'):
        return {"breadcrumbs" : request.breadcrumbs}
    else:
        return {}
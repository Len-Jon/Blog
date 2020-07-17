from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from superadmin import models
from user.models import User


def redirectTo(request):
    return HttpResponseRedirect('/admin/index')


def login(request):
    return render(request, 'superadmin/login.html')


@csrf_exempt
def doLogin(request):
    """
    接受登陆信息并返回结果
    :param request: request
    :return: 判断密码是否正确
    """
    m = models.Admin.objects.get(name=request.POST['name'])
    if m.password == request.POST['password']:
        request.session['super_id'] = m.id
        request.session['name'] = m.name
        return HttpResponse("True")
    else:
        return HttpResponse("Your username and password didn't match.")


def index(request):
    return render(request, 'superadmin/index.html')


def userList(request):
    return render(request, 'superadmin/userList.html', {'users': User.objects.all()})


def monitor(request, user_id):
    request.session['id'] = int(user_id)
    return render(request, 'superadmin/monitor.html', {'url': '/user/index'})

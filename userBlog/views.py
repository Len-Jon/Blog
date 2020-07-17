from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from user import models


def login(request):
    """
    :param request: request
    :return: 返回登陆页面
    """
    return render(request, 'user/login.html')


@csrf_exempt
def doLogin(request):
    """
    接受登陆信息并返回结果
    :param request: request
    :return: 判断密码是否正确
    """
    m = models.User.objects.get(name=request.POST['name'])
    if m.password == request.POST['password']:
        request.session['id'] = m.id
        request.session['name'] = m.name
        return HttpResponse("True")
    else:
        return HttpResponse("Your username and password didn't match.")


def index(request):
    return render(request, 'cleanblog/index.html',
                  {'items': models.Article.objects.filter(author_id=request.session['id'])})


def page(request, ID):
    obj = models.Article.objects.get(id=ID)
    if obj.author_id != request.session['id']:
        pass
    return render(request, 'cleanblog/page.html', {'item': obj})


def logout(request):
    """
    登出请求
    :param request: request
    :return: 重定向至login
    """
    # request.session.clear()  # 清空的是值
    response = redirect('/user/login')
    response.delete_cookie('sessionid')
    # request.session.flush()  # 键和值一起清空
    return response


def register(request):
    return render(request, 'user/register.html')


@csrf_exempt
def doRegister(request):
    user = models.User.objects.filter(name=request.POST['name'])
    # print(user)
    if user:
        print(user)
        return HttpResponse("用户已存在")
    else:
        pass
        models.User.objects.create(name=request.POST['name'], password=request.POST['password'])
    return HttpResponse('True')


def page(request, ID):
    if request.session['id'] != int(ID):
        return render(request, '404.html')
    obj = models.Article.objects.get(id=ID)
    return render(request, 'cleanblog/page.html', {'item': obj})


def redirectTo(request):
    return HttpResponseRedirect('/user/index')

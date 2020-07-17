import uuid

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from blog import settings
from user import models


def redirectToLogin(request):
    return HttpResponseRedirect('/user/admin/index/')


def index(request):
    """
    :param request: request
    :return: 返回管理员主页
    """
    return render(request, "userAdmin/index.html")


"""
公用接口
"""


def imgUpload(img):
    img_uuid = str(uuid.uuid1())
    img_end = img.name.split('.')[-1]
    filename = '%s/upload/%s' % (settings.MEDIA_ROOT, img_uuid + '.' + img_end)
    with open(filename, 'wb') as pic:
        for c in img.chunks():
            pic.write(c)
    return '/media/upload/' + img_uuid + '.' + img_end


@csrf_exempt
def uploadArticle(request):
    """
    :param request:
    :return: 将文章上传到数据库
    """
    models.Article.objects.create(title=request.POST['title'], articleType=request.POST['articleType'],
                                  content=request.POST['content'], author_id=request.session['id'])
    return HttpResponse('ok')


@csrf_exempt
def doUploadArticle(request):
    """
    :param request:
    :return: 将文章更新到数据库
    """

    item = models.Article.objects.get(id=request.POST['id'])
    if request.session['id'] != item.author_id:
        return render(request, '404.html')
    item.title = request.POST['title']
    item.content = request.POST['content']
    item.save()
    return HttpResponse('ok')


@csrf_exempt
@xframe_options_exempt
def uploadImg(request):
    """
    markdown图片上传
    :param request:
    :return:
    """
    img = request.FILES['editormd-image-file']
    url = imgUpload(img)
    return JsonResponse({'success': 1, 'message': "上传成功", 'url': url})


@csrf_exempt
@xframe_options_exempt
def uploadImage(request):
    """
    rtf图片上传
    :param request:
    :return:
    """
    img = request.FILES['upload_file']
    url = imgUpload(img)
    return JsonResponse({'success': 1, 'msg': 'error message', 'file_path': url})


"""
Markdown
"""


def new_markdown(request):
    """
    :param request:
    :return: 返回新markdown文章
    """
    return render(request, 'userAdmin/new_markdown.html')


def markdownList(request):
    """
    :param request:
    :return: 返回文章列表页面
    """
    return render(request, 'userAdmin/article_list.html',
                  {'sign': 0, 'items': models.Article.objects.filter(articleType=0, author_id=request.session['id'])})


def deleteMarkdown(request, ID):
    """
    删除Markdown
    :param ID: 文章id
    :param request:
    :return: 返回文章列表页面
    """
    if request.session['id'] == int(ID):
        models.Article.objects.filter(id=ID).delete()
    return render(request, 'userAdmin/article_list.html',
                  {'sign': 0, 'items': models.Article.objects.filter(articleType=0, author_id=request.session['id'])})


def updateMarkdown(request, ID):
    """
    :param request:
    :param ID: 文章id
    :return:
    """
    if request.session['id'] != int(ID):
        return render(request, '404.html')
    obj = models.Article.objects.get(id=ID)
    content = obj.content.replace('"', r'\"').replace('\n', r'\n').replace('/', '\\/')
    # .replace('<', '&#lt;').replace('>', '&#gt;')  # 因为前端用的是双引号把字符包裹起来，所以只用转义这个
    return render(request, 'userAdmin/update_markdown.html', {'item': obj, 'content': content})


"""
rich text format
"""


def new_rtf(request):
    return render(request, 'userAdmin/new_rtf.html')


def rtfList(request):
    return render(request, 'userAdmin/article_list.html',
                  {'sign': 1, 'items': models.Article.objects.filter(articleType=1, author_id=request.session['id'])})


def deleteRtf(request, ID):
    """
    删除Markdown
    :param ID: 文章id
    :param request:
    :return: 返回文章列表页面
    """
    if request.session['id'] == int(ID):
        models.Article.objects.filter(id=ID).delete()
    return render(request, 'userAdmin/article_list.html',
                  {'sign': 1, 'items': models.Article.objects.filter(articleType=1, author_id=request.session['id'])})


def updateRtf(request, ID):
    """
    :param request:
    :param ID: 文章id
    :return:
    """
    if request.session['id'] != int(ID):
        return render(request, '404.html')
    obj = models.Article.objects.get(id=ID)
    content = obj.content.replace('"', r'\"')  # 因为前端用的是双引号把字符包裹起来，所以只用转义这个
    return render(request, 'userAdmin/update_rtf.html', {'item': obj, 'content': content})

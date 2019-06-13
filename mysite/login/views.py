from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
'''
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        models.Userinfo.objects.create(username=username, password=password)

    # 创建分页
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    # 获取数据
    bug = models.Userinfo.objects.all()

    # 取到最新5条数据
    top5 = models.Userinfo.objects.order_by('-id')[:5]

    # 开始分页
    paginator = Paginator(bug.order_by('-id'), 10)
    page_num = paginator.num_pages

    page_bug_list = paginator.page(page)

    if page_bug_list.has_next():
        next_page = page + 1
    else:
        next_page = page

    if page_bug_list.has_previous():
        previous = page - 1
    else:
        previous = 1

    # return render(request, 'index11.html', {'temp': user_list})
    return render(request, 'index11.html',
                  {'user_list': page_bug_list,
                   'page_num': range(1, page_num + 1),
                   'curr_page': page,
                   'next_page': next_page,
                   'previous': previous,
                   'top5': top5,
                   }
                  )


def delete(request, user_id):
    models.Userinfo.objects.filter(id=user_id).delete()
    return redirect('/login')
'''


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('/host')
            else:
                return HttpResponse("请输入正确的用户名和密码")
        else:
            return HttpResponse("输入无效")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login/login.html', {"form": login_form})


def user_logout(request):
    response = redirect('/login/')
    response.delete_cookie('username')
    return response

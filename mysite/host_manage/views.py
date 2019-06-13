from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Host

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    # 创建分页
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    host = Host.objects.all()

    top5 = Host.objects.order_by('-id')[:5]
    # 开始分页
    paginator = Paginator(host.order_by('-id'), 15)
    page_num = paginator.num_pages

    host_list = paginator.page(page)

    if host_list.has_next():
        next_page = page + 1
    else:
        next_page = page

    if host_list.has_previous():
        previous = page - 1
    else:
        previous = 1
    return render(request, 'host_manage/index.html',
                  {'host': host_list,
                   'page_num': range(1, page_num + 1),
                   'curr_page': page,
                   'next_page': next_page,
                   'previous': previous,
                   'top5': top5,
                   }
                  )


@login_required
def delete(request, host_id):
    Host.objects.filter(id=host_id).delete()
    return redirect('/host')

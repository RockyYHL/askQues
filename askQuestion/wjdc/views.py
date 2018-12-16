from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.
#首页
@csrf_exempt
def index(request):
    return render(request, 'index.html', )  # 将绑定的数据传入前台

@csrf_exempt
def parents(request):
    return render(request, 'B_RT-info.html', )  # 将绑定的数据传入前台


@csrf_exempt
def parents2(request):
    return render(request, 'B_RT-1.html', )  # 将绑定的数据传入前台

@csrf_exempt
def parents3(request):
    return render(request, 'B_RT-2.html', )  # 将绑定的数据传入前台

@csrf_exempt
def parents4(request):
    return render(request, 'B_RT-3.html', )  # 将绑定的数据传入前台

@csrf_exempt
def endpage(request):
    return render(request, 'endpage.html', )  # 将绑定的数据传入前台

@csrf_exempt
def test(request):
    return render(request, 'test.html', )  # 将绑定的数据传入前台


@csrf_exempt
def students(request):
    return render(request, 'B_XS-info.html', )  # 将绑定的数据传入前台

@csrf_exempt
def students2(request):
    return render(request, 'B_XS-1.html', )  # 将绑定的数据传入前台

@csrf_exempt
def students3(request):
    return render(request, 'B_XS-2.html', )  # 将绑定的数据传入前台

@csrf_exempt
def students4(request):
    return render(request, 'B_XS-3.html', )  # 将绑定的数据传入前台

@csrf_exempt
def adult(request):
    return render(request, 'B_CR-info.html', )  # 将绑定的数据传入前台

@csrf_exempt
def adult2(request):
    return render(request, 'B_CR-1.html', )  # 将绑定的数据传入前台

@csrf_exempt
def adult3(request):
    return render(request, 'B_CR-2.html', )  # 将绑定的数据传入前台

@csrf_exempt
def adult4(request):
    return render(request, 'B_CR-3.html', )  # 将绑定的数据传入前台

#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db import connection 
from django.views.generic.base import TemplateView
from .forms import ContactForm,BlogForm
from django.contrib.auth.decorators import login_required  
# Create your views here.
# python 不要带分号 注意缩进  if for while 等语句块用冒号
class loginFormView(FormView):
    template_name = 'loginApp/login.html'
    form_class = ContactForm

class registerFormView(FormView):
    template_name = 'loginApp/register.html'
    form_class = ContactForm

def checkRegisterView(request):
    username = request.POST['username']
    passwd = request.POST['passwd']
    passwd_repeat = request.POST['passwd_repeat']
    if passwd_repeat != passwd or not username or not passwd:
        return HttpResponseRedirect('/login/register')
    # cursor = connection.cursor()  # 数据库操作
    # cursor.excute("select username from auth_user where username=%"%username)
    res = User.objects.filter(username=username)
    if len(res) == 0:
        user = User.objects.create_user(username=username,password=passwd)
        user.save()
        return HttpResponseRedirect('/login/login')
    else:
        return HttpResponseRedirect('/login/register')
def checkLoginView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/login/space')
    else:
        uname = request.POST['username']
        passwd = request.POST['passwd']
        print("%s %s"%(uname,passwd))
        user = authenticate(username='xuxing', password='123456')
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/login/space')
        else:
            # return render(request,'loginApp/welcome.html')
            return HttpResponseRedirect('/login/register')

@login_required
def spaceView(request):
    if request.method == 'GET':
        form = BlogForm()
        user = request.user
        return render(request, 'loginApp/space.html', {'form_blog':form,'user':user})

    else :
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)  # 返回对象但是不会保存到数据库中
            form.author = request.user
            form.save();
            return render(request,'loginApp/welcome.html')
        else :
            return render(request, 'loginApp/space.html',{'form_blog':BlogForm,'user':reuqest.user})


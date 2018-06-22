from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django import forms
from silo.models import User
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    #email = forms.EmailField(label='邮箱')

def silo(request):
    return HttpResponse("Hello, world. You're at the silo index.")

def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            #email = userform.cleaned_data['email']
            #user = User.objects.create(username=username,password=password,email=email)
            user = User.objects.create(username=username,password=password)
            user.save()

            return HttpResponse('regist success!!!')
    else:
        userform = UserForm()
        return render_to_response('regist.html',{'userform':userform})

def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username,password__exact=password)

            if user:
                #return render_to_response('index.html',{'userform':userform})
                return HttpResponseRedirect("http://203.195.237.245:56778")
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
        return render_to_response('login.html',{'userform':userform})

def index(request):
    userform=UserForm()
    return render_to_response('index.html',{'userform':userform})

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import User

# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'AppTwo/help.html',context=helpdict)

def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'AppTwo/users.html',context=user_dict)



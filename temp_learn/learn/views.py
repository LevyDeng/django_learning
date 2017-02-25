#coding:utf-8
from django.shortcuts import render

# Create your views here.
def home(request):
    learn_text='努力学习django'
    learn_list=['lalala','python','123']
    learn_range=range(100)
    #return render(request,'learn/home.html',{'learn_list':learn_list},{'learn_text':learn_text})
    return render(request,'learn/home.html',{'learn_range':learn_range})


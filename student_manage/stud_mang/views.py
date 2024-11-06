from django.shortcuts import render,redirect
from .models import *

# Create your views here.
std=[{'rollno':'1','name':'anu','age':'21'},{'rollno':'2','name':'anita','age':'22'},{'rollno':'3','name':'harry','age':'22'}]

def home(req):
    if req.method=='POST':
        roll=req.POST['rollno']
        name=req.POST['name']
        age=req.POST['age']
        mark=req.POST['mark']
        address=req.POST['address']
        # std.append({'rollno':roll,'name':name,'age':age})
        data=Student.objects.create(rollno=roll,name=name,age=age,mark=mark,address=address)
        data.save()
        return redirect(home)
    else:
        data=Student.objects.all()
        return render(req,'home.html',{'students':data})
    
def Edit_std(req,id):
    # data=''
    # for i in std:
    #         if i['id']==id:
    #                 data=i
    if req.method=='POST'    :
            roll=req.POST['rollno']
            name=req.POST['name']
            age=req.POST['age']
            mark=req.POST['mark']
            address=req.POST['address']
            Student.objects.filter(pk=id).update(rollno=roll,name=name,age=age,mark=mark,address=address)
            return redirect(home)
    else:
            data=Student.objects.get(pk=id)
            return render(req,'edit.html',{'data':data})
    
def Delete(req,id):
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(home)          
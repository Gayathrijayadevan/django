from django.shortcuts import render,redirect

# Create your views here.
std=[{'rollno':'1','name':'anu','age':'21'},{'rollno':'2','name':'anita','age':'22'},{'rollno':'3','name':'harry','age':'22'}]

def home(req):
    if req.method=='POST':
        roll=req.POST['rollno']
        name=req.POST['name']
        age=req.POST['age']
        std.append({'rollno':roll,'name':name,'age':age})
        return redirect(home)
    else:
        return render(req,'home.html',{'students':std})
    
def Edit_std(req,a):
    data=''
    for i in std:
            if i['rollno']==a:
                    data=i
    if req.method=='POST'    :
            roll=req.POST['rollno']
            name=req.POST['name']
            age=req.POST['age']

            data['rollno']=roll
            data['name']=name
            data['age']=age
            return redirect(home)

    else:
            return render(req,'edit.html',{'data':data})
    
def Delete(req,a):
    for i in std:
            if i['rollno']==a:
                std.remove(i)
    return redirect(home)          
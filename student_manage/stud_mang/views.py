from django.shortcuts import render,redirect

# Create your views here.
std=[]

def home(req):
    if req.method=='POST':
        roll=req.POST['rollno']
        name=req.POST['name']
        age=req.POST['age']
        std.append({'rollno':roll,'name':name,'age':age})
        return redirect(home)
    else:
        return render(req,'home.html',{'students':std})

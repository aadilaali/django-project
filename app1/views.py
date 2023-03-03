from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import RegisterForm,LoginForm,UpdateForm,ChangePasswordForm,GalleryForm
from . models import Register1,Gallery
from django.contrib import messages
from django.contrib.auth import logout as logouts
# Create your views here.
def hello(request):
    return HttpResponse("WELCOME TO PROJECT1")

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            user=Register1.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"Alreday exists")
                return redirect('/signup')
            elif password!=confirmpassword:
                messages.warning(request,"Password Mismatch")
                return redirect('/signup')
            else:
                tab=Register1(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"Success")
                return redirect('/login')
    else:
        form=RegisterForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Register1.objects.get(Email=email)
                if not user:
                    messages.warning(request,"Does not exist")
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,"Incorrect Password")
                    return redirect('/login')
                else:
                    messages.success(request,"Success")
                    return redirect('/home/%s' %user.id)
            except:

                messages.warning(request,"username or password incorrect")
                return redirect('/login')
    else:
        form=LoginForm
    return render(request,'login.html',{'form':form})

def home(request,id):
    data=Register1.objects.get(id=id)
    return render(request,'home.html',{'data':data})

def update(request,id):
    data=Register1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"updated")
            return redirect('/home/%s' % data.id)
    else:
        form=UpdateForm(instance=data)
    return render(request,'update.html',{'data':data,'form':form})

def changepassword(request,id):
    data=Register1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=data.Password:
                messages.warning(request,"Incorrect")
                return redirect('/changepassword/%s' % data.id)
            elif oldpassword==newpassword:
                messages.warning(request,"Similar")
                return redirect('/changepassword/%s' % data.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"Mismatch")
                return redirect('/changepassword/%s' % data.id)
            else:
                data.Password=newpassword
                data.save()
                messages.success(request,"Success")
                return redirect('/home/%s' % data.id)
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form})

def logout(request):
    logouts(request)
    messages.success(request,"Logged out successfully")
    return redirect('/')

def details(request,id):
    user=Gallery.objects.get(id=id)
    return render(request,'details.html',{'user':user})

def gallery1(request):
    users=Gallery.objects.all()
    return render(request,'gallery1.html',{'users':users})

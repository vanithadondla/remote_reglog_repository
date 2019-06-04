from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse

def registration_view(request):
    if request.method=="POST":
        rform =RegistrationForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name', '')
            mobile = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            username = request.POST.get('username', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')

            data=RegistrationData(
                 first_name=first_name,
                 last_name=last_name,
                 mobile = mobile,
                 email = email,
                 username =username,
                 password1=password1,
                 password2=password2,
            )
            data.save()
            lform=LoginForm()
            return render(request,'login.html',{'lform':lform})
        else:
            rform=RegistrationForm()
            return render(request,'registration.html',{'rform':rform})
    else:
            rform=RegistrationForm()
            return render(request,'registration.html',{'rform':rform})
def login_view(request):
    pass
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            uname=request.POST.get('username','')
            pwd=request.POST.get('password1','')
            uname1=RegistrationData.objects.filter(username=uname)
            pwd1=RegistrationData.objects.filter(password1=pwd)
            if uname1 and pwd1:
                return HttpResponse("valid Details")
            else:
                return HttpResponse("Invalid Details")

    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})





from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

@login_required(login_url='/login/')
def homepage(request):        

    
    return render(request,"index.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        try:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("dashboard")
            else:
                print("User is None ")
        except BaseException as e:
            print(e)
        
            
    return render(request,"login.html")

def logout_(request):
    if request.user:
        logout(request)
        return redirect("login")
    else:
        pass

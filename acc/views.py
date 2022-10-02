from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from acc.models import User
from django.contrib import messages

# Create your views here.
def update(request):
    if request.method == "POST":
        u = request.user
        up = request.FILES.get("upic")
        uc = request.POST.get("ucomm")
        cp = request.POST.get("upass")
        wp = request.POST.get("newpass")
        if check_password(cp, u.password):
            u.set_password(wp)
            u.save()
            return redirect('acc:login')
        if up:
            u.pic = up
        u.comment = uc
        u.save()
        return redirect('acc:index')
    return render(request, "acc/update.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
        return redirect('acc:login')
    return render(request, "acc/signup.html")

def profile(request):
    if request.method == "POST":
        u = request.user
        up = request.POST.get("upass")
        nowpass = u.password
        if check_password(up, nowpass):
            return redirect("/acc/delete")
    return render(request, "acc/profile.html")

def delete(request):
    # if request.method == "POST":
    #     u = request.user
    #     up = request.POST.get("pwck")
    #     cpass = u.password
    #     if check_password(up, cpass):
    #         request.user.delete()
    #         return redirect('acc:index')
    request.user.pic.delete()
    request.user.delete()
    return redirect('acc:index')


def index(request):
    return render(request, "acc/index.html")

def userlogout(request):
    logout(request)
    return redirect("acc:login")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f"{un} 님 환영합니다")
            return redirect("acc:index")
        else:
            messages.error(request, "계정정보가 없습니다")
    return render(request, "acc/login.html")

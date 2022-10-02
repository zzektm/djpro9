
from django.shortcuts import render, redirect

from vote.models import Choice, Topic
# Create your views here.


def index(request):
    t = Topic.objects.all()
    context = {
        'tset' : t
    }

    return render(request, "vote/index.html", context)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        'cset' : c,
        't' : t
    }
    return render(request, 'vote/detail.html', context)

def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get('cho')
        c = Choice.objects.get(id=cpk)
        c.choicer.add(request.user)
    return redirect("vote:detail", tpk)

def cancel(request, tpk):
    u = request.user
    t = Topic.objects.get(id=tpk)
    t.voter.remove(u)
    u.choice_set.get(topic=t).choicer.remove(u)
    return redirect("vote:detail", tpk)

def create(request):
    if request.method == "POST":
        s = request.POST.get('sub')
        c = request.POST.get('con')
        t = Topic(subject = s, maker=request.user, content = c)
        t.save()
        cn = request.POST.get('cname')
        cc = request.POST.get('ccomm')
        for name, com in zip(cn, cc):
            Choice(topic = t, name = name, comment = com).save()
        return redirect("vote:index")
    return render(request, 'vote/create.html')

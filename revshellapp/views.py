from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")
def enter(request):
    if request.method == "POST":
        from . import models
        obj = models.commands()
        obj.cmd = request.POST.get("cmd")
        obj.save()
    return render(request, "test.html")
def response(request):
    return render(request, "response.html")
def enterres(request):
    if request.method == "POST":
        from . import models
        obj = models.text()
        obj.text = request.POST.get("text")
        obj.save()
    
    return redirect("response")
def showcmds(request):
    from .models import commands
    obj = commands.objects.all()
    length = len(obj)
    return render(request, "showcmds.html", {"cmd" : obj[length-1].cmd})
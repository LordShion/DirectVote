from django.shortcuts import render

def home(request):
    print "home"
    return render(request,'home.html',{'data':''})
    
def login(request):
    print "login"
    return render(request,'login.html',{'data':''})
    
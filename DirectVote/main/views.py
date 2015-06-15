from django.shortcuts import render
from django.http import HttpResponse
import json

def home(request):
    print "home"
    return render(request,'home.html',{'data':''})
    
def login(request):
    print "login"
    return render(request,'login.html',{'data':''})

def loginsubmit(request):
    print "login submit"
    response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = 'you are logged'

    return HttpResponse(json.dumps(response_data), content_type="application/json")
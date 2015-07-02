from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect



import json
import base64

from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required

@require_GET
#@login_required
def home(request):
    print("home")
    logged = False
    if not request.user.is_authenticated():
        print ("redirecting")
        #return redirect('/login')
        logged = False
    else: 
        print("true")
        logged = True
    return render(request,'home.html',{'logged':logged})

@require_GET
def loginUser(request):
    print ("login")
    return render(request,'login.html')

@require_POST
def loginSubmit(request):
    print("login submit")
    try: 
        data = json.loads(request.body.decode('utf-8'))
    except Exception as s:
        return HttpResponse(json.dumps({'message':'error reading json'}), content_type='application/json',status=400)
    #print data
    #print data['pass']
    #print base64.b64decode(data['pass'])
    
    user = authenticate(username = data['user'], password = base64.b64decode(data['pass'])) 
    #print user.username
    #print user.password
    
    response_data = {}
    
    if user is not None:
        # the password verified for the user
        if user.is_active:
            #print("User is valid, active and authenticated")
            login(request, user)
            #return redirect('/')
            
            response_data['result'] = 'success'
            response_data['message'] = 'you are logged'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
            
        else:
            #print("The password is valid, but the account has been disabled!")
            response_data['result'] = 'fail'
            response_data['message'] = 'account disabled, you are not logged'
            return HttpResponse(json.dumps(response_data), content_type="application/json",status=403)
    else:
        # the authentication system was unable to verify the username and password
        #print("The username and password were incorrect.")
        response_data['result'] = 'fail'
        response_data['message'] = 'username and/or password incorrect, you are not logged'
        return HttpResponse(json.dumps(response_data), content_type="application/json",status=403)
    

    response_data['result'] = 'fail'
    response_data['message'] = 'unknown error, you are not logged'

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=403)


@require_POST
def logoutUser(request):
    logout(request)
    response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = 'you have been logged out'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@require_GET
def viewPage(request, page):
    print(page+".html")
    
    return render(request, page+".html" )
    
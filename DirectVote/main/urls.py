#-*- coding:utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns('',
    
    url(r'^login/submit', 'DirectVote.main.views.loginSubmit', name='main.loginSubmit'),
    url(r'^login', 'DirectVote.main.views.loginUser', name='main.loginUser'),
    url(r'', 'DirectVote.main.views.home', name='main.home'),
    

)


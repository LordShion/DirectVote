#-*- coding:utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns('',
    
    url(r'^login/submit', 'DirectVote.main.views.loginsubmit', name='main.loginsubmit'),
    url(r'^login', 'DirectVote.main.views.login', name='main.login'),
    url(r'', 'DirectVote.main.views.home', name='main.home'),
    

)


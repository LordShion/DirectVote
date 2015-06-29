#-*- coding:utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns('',
    
    url(r'^login/submit', 'DirectVote.main.views.loginSubmit', name='main.loginSubmit'),
    url(r'^login', 'DirectVote.main.views.loginUser', name='main.loginUser'),
    url(r'^logout', 'DirectVote.main.views.logoutUser', name='main.logoutUser'),
    url(r'^view/(?P<page>[\w,\s-]+\.[A-Za-z]{4}$)$', 'DirectVote.main.views.viewPage', name='main.viewPage'),
    
    url(r'', 'DirectVote.main.views.home', name='main.home'),
    

)


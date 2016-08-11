from django.conf.urls import include, url
from django.contrib import admin
from django.views.i18n import set_language



urlpatterns = [
    # Examples:
    # url(r'^$', 'DirectVote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('allauth.urls')),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
    url('^i18n/setlang/$', set_language),
    
    url(r'', include('DirectVote.main.urls')),
    
    
]


from django.conf.urls import include, url
from django.contrib import admin




urlpatterns = [
    # Examples:
    # url(r'^$', 'DirectVote.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('allauth.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')), 
    url(r'', include('DirectVote.main.urls')),
    
    
]


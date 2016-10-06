from django.conf.urls import  include, url
from django.contrib import admin
from exercise.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'workout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home,name="home"),
]

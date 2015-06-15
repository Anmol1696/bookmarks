from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from book.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'book_marks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',main_page),
    url(r'^user/(\w+)/$',user_page),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$',logout_page),
)

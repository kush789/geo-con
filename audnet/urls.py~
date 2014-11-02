from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'audnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^logout/', 'audnet.views.logout'),
    url(r'^auth/', 'audnet.views.auth_view'),

    url(r'^user/register/', 'audnet.views.register'),

    url(r'^$', 'audnet.views.index', name='home'), #index page
    (r'^user/', include('posts.urls')),	


)

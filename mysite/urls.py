from django.conf.urls import patterns, include, url
from django.contrib import admin
from exchange import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^exchange', include('exchange.urls')),
    url(r'^register/', views.register,name='register'),
    url(r'^account/', views.account,name='account'),
    url(r'^login/', views.login,name='login'),
    url(r'^logout/', views.logout,name='logout'),
    url(r'^viewUser/(?P<user_id>\d+)/$', views.viewUser,name='viewUser'),
    url(r'^$',views.index,name='index'),

)

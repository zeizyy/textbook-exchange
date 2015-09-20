from django.conf.urls import patterns, url

from exchange import views

urlpatterns = patterns('',
	url(r'^/$', views.index, name='index'),
	url(r'^/viewBook/(?P<book_id>\d+)/$', views.viewBook, name='viewBook'),
	url(r'^/viewRequest/(?P<request_id>\d+)/$', views.viewRequest, name='viewRequest'),
	url(r'^/searchBook/$', views.searchBook, name='searchBook'),
	url(r'^/createBook/$', views.createBook, name='createBook'),
	url(r'^/createRequest/$', views.createRequest, name='createRequest'),
	url(r'^/deleteBook/(?P<book_id>\d+)/$', views.deleteBook, name='deleteBook'),
	url(r'^/deleteRequest/(?P<request_id>\d+)/$', views.deleteRequest, name='deleteRequest'),
	url(r'^/editBook/(?P<book_id>\d+)/$', views.editBook, name='editBook'),
	url(r'^/editRequest/(?P<request_id>\d+)/$', views.editRequest, name='editRequest'),
	url(r'^/addContact/$', views.addContact, name='addContact'),
	url(r'^/requestAll/$', views.requestAll, name='requestAll'),
	url(r'^/guess/$', views.guess, name='guess'),
	url(r'^/add/$', views.add, name='add'),
	url(r'^/bookAll/$', views.bookAll, name='bookAll'),
	url(r'^/userAll/$', views.userAll, name='userAll'),
	url(r'^/share/(?P<user_id>\d+)/$', views.share, name='share'),

)
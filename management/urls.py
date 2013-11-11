# - coding:utf-8 -
from django.conf.urls import patterns, url, include
from django.views.generic import list_detail
from django.contrib.auth.models import User
from management.models import AttendList
import datetime

#汎用ビューを使っている部分は後で書きなおす
urlpatterns = patterns('',
	url(r'^$', 'management.views.redirect_index'),
	url(r'^attend/$', 'management.views.redirect_loginpage'),
	url(r'^login/$', 'management.views.login_user'),
	url(r'^add/$', 'management.views.redirect_addpage'),
	url(r'^useradd/$', 'management.views.add_user'),
	url(r'^userlist/$', list_detail.object_list, dict({ "queryset" : User.objects.all() }, template_name = "management/userlist.html")),
	url(r'^attendlist/$', list_detail.object_list,dict( { "queryset" : AttendList.objects.filter(attendtime = datetime.date.today()) }, 
		template_name = "management/attendlist.html")),
)

# - coding:utf-8 -

#from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from management.models import AttendList, AttributeList
import datetime
# Create your views here.

#トップページへのリダイレクト
def redirect_index(request):
	return render_to_response('management/index.html')

#ログイン用ページへのリダイレクト
#CSRF対策は忘れずに
def redirect_loginpage(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('management/login.html', c)

#ユーザー登録ページへのリダイレクト
#CSRF対策は忘れずに
def redirect_addpage(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('management/useradd.html', c)

#ユーザーの登録処理
def add_user(request):
	#フォームに入力された情報の取得
	userid = request.POST['userid']
	password = request.POST['pass']
	rpassword = request.POST["rpass"]
	fname = request.POST['fname']
	lname = request.POST['lname']
	gender = request.POST['gender']
	number = request.POST['number']

	#表示用メッセージ
	message = ""

	#useridの重複チェック
	try:
		User.objects.get(username = userid)
		message = u"そのIDは既に使用されています"
		#return render_to_response('management/success.html', message)
	except User.DoesNotExist:
		if password != rpassword:
			message = u"パスワードが間違っています"
		else:
			user = User.objects.create_user(username = userid, password = password)
			user.save()
			add_al = AttributeList(user = user, gender = gender, number = number, first_name = fname, last_name = lname)
			add_al.save()
			message = "ユーザー登録が完了しました"
	return render_to_response('management/success.html', {'message' : message})

#ユーザーのログイン処理（出席用）
#今のところ出席のみに使用
def login_user(request):
	#入力されたIDとパスワードを取得
	userid = request.POST['userid']
	password = request.POST['pass']
	
	#IDとパスワードに応じたユーザーが存在するか確認
	user = authenticate(username=userid, password=password)

	#表示用メッセージ
	message = ""
	
	if user is None:
		message = "そのようなユーザーは存在していません"
	else:
		if user.is_active:
			try:
				AttendList.objects.get(user = user,attendtime = datetime.date.today())
				message = "すでに出席済みです"
			except AttendList.DoesNotExist:
				login(request,user)
				attend = AttendList(user = user)
				attend.save()
				message = "出席が確認されました"
				logout(request)
	return render_to_response('management/success.html', {'message' : message})


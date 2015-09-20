#coding=utf-8 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from exchange.models import Book, User, Request
from exchange.forms import BookForm, RequestForm
#csrf exempt
from django.views.decorators.csrf import csrf_exempt

from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		return render_to_response('exchange/index.html',{'guest':True})
	if user.username == 'zeizyy1123':
		admin = True
	else:
		admin = False
	books = Book.objects.all().filter(sold=False)
	requests = Request.objects.all().filter(bought=False)
	user = User.objects.get(pk=user_id)
	books_user = books.filter(user=user)
	for book in books_user:
		zitou = book.zitou
		kehao = book.kehao
		r = requests.filter(zitou__icontains=zitou).filter(kehao=kehao)
		if r:
			return render_to_response('exchange/index.html',{'match':True,'icon':True,'admin':admin})

	requests_user = requests.filter(user=user)
	for req in requests_user:
		zitou = req.zitou
		kehao = req.kehao
		b = books.filter(zitou__icontains=zitou).filter(kehao=kehao)
		if b:
			return render_to_response('exchange/index.html',{'match':True,'icon':True,'admin':admin})
	return render_to_response('exchange/index.html',{'icon':True,'admin':admin})

def requestAll(request):
	requests = Request.objects.all().filter(bought=False)
	return render_to_response('exchange/requestAll.html',{'requests':requests})

def bookAll(request):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		return render_to_response('exchange/bi.html')
	if not user.username == 'zeizyy1123':
		return render_to_response('exchange/bi.html')
	books = Book.objects.all().filter(sold=False)
	return render_to_response('exchange/requestAll.html',{'requests':books,'seller':True})

def userAll(request):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		return render_to_response('exchange/bi.html')
	if not user.username == 'zeizyy1123':
		return render_to_response('exchange/bi.html')
	users = User.objects.all()
	return render_to_response('exchange/userAll.html',{'users':users})


def guess(request):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		return HttpResponseRedirect(reverse('exchange.views.login'))
	books_rec = []
	requests_rec = []
	books = Book.objects.all().filter(sold=False)
	requests = Request.objects.all().filter(bought=False)
	user_id = request.session['current_user']
	user = User.objects.get(pk=user_id)
	books_user = books.filter(user=user)
	for book in books_user:
		zitou = book.zitou
		kehao = book.kehao
		r = requests.filter(zitou__icontains=zitou).filter(kehao=kehao)
		requests_rec.extend(r)
	requests_user = requests.filter(user=user)
	for req in requests_user:
		zitou = req.zitou
		kehao = req.kehao
		b = books.filter(zitou__icontains=zitou).filter(kehao=kehao)
		books_rec.extend(b)
	books_rec = list(set(books_rec))
	requests_rec = list(set(requests_rec))
	if not books_rec and not requests_rec:
		return render_to_response('exchange/none.html')
	return render_to_response('exchange/guess.html',{'books_rec':books_rec,'requests_rec':requests_rec})

def add(request):
	return render_to_response('exchange/bookForm.html')

def viewBook(request,book_id):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		user = ""
	book = Book.objects.get(pk=book_id)
	zitou = book.zitou
	kehao = book.kehao
	rec = Book.objects.filter(zitou__icontains=zitou).filter(kehao=kehao).exclude(pk=book_id)[:5]
	book.count = book.count + 1
	book.save()
	return render_to_response('exchange/viewBook.html',{'book':book,'rec':rec,'user':user,'icon':True})

@csrf_exempt	
def editBook(request, book_id):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		user = ""
	try:
		book = Book.objects.get(id=book_id)
	except Book.DoesNotExist:
		raise Http404("The textbook does not exist！")
	if book.user == user:
		if request.POST:
			book_form = BookForm(request.POST,instance=book)
			if book_form.is_valid():
				book = book_form.save()
				book.save()
				return HttpResponseRedirect(reverse('exchange.views.viewBook',args=[book.id]))
		else:
			book_form = BookForm(instance=book)
	else:
		return render_to_response('exchange/bi.html')
	return render_to_response('exchange/editBook.html',{'book_form':book_form,'book':book})


def viewRequest(request,request_id):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		user = ""
	request = Request.objects.get(pk=request_id)
	request.count = request.count + 1
	request.save()
	return render_to_response('exchange/viewRequest.html',{'request':request,'user':user,'icon':True})

def deleteRequest(request,request_id):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		user = ""
	requests = Request.objects.get(pk=request_id)
	if user == requests.user:
		requests.bought = not requests.bought
		requests.save()
		return HttpResponseRedirect(reverse('exchange.views.index'))
	else:
		return render_to_response('exchange/bi.html')

@csrf_exempt	
def editRequest(request, request_id):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		user = ""
	try:
		requests = Request.objects.get(id=request_id)
	except Request.DoesNotExist:
		raise Http404("The request does not exist!")
	if requests.user == user:
		if request.POST:
			request_form = RequestForm(request.POST,instance=requests)
			if request_form.is_valid():
				requests = request_form.save()
				requests.save()
				return HttpResponseRedirect(reverse('exchange.views.viewRequest',args=[requests.id]))
		else:
			request_form = RequestForm(instance=requests)
	else:
		return render_to_response('exchange/bi.html')
	return render_to_response('exchange/editRequest.html',{'request_form':request_form,'request':requests})


@csrf_exempt
def searchBook(request):
	zitou = request.POST['zitou']
	zitou = zitou.upper()
	kehao = request.POST['kehao']
	try:
		switch = request.POST['switch']
	except:
		switch = None
	
	if switch:
		if zitou and kehao:
			books = Book.objects.filter(zitou__icontains=zitou).filter(kehao=kehao)
		elif zitou:
			books = Book.objects.filter(zitou__icontains=zitou)
		elif kehao:
			books = Book.objects.filter(kehao=kehao)
		else:
			return HttpResponseRedirect('/')
		books = books.filter(sold=False)
		if not books:
			try:
				user_id = request.session['current_user']
				user = User.objects.get(pk=user_id)
			except:
				return HttpResponseRedirect(reverse('exchange.views.login'))
			book_form = RequestForm(initial={'zitou':zitou,'kehao':kehao})
			return render_to_response('exchange/createBook.html',{'book_form':book_form})
	else:
		if zitou and kehao:
			books = Request.objects.filter(zitou__icontains=zitou).filter(kehao=kehao)
		elif zitou:
			books = Request.objects.filter(zitou__icontains=zitou)
		elif kehao:
			books = Request.objects.filter(kehao=kehao)
		else:
			return HttpResponseRedirect('/')
		books = books.filter(bought=False)
		if not books:
			try:
				user_id = request.session['current_user']
				user = User.objects.get(pk=user_id)
			except:
				return HttpResponseRedirect(reverse('exchange.views.login'))
			book_form = BookForm(initial={'zitou':zitou,'kehao':kehao})
			return render_to_response('exchange/createRequest.html',{'book_form':book_form})
	
	return render_to_response('exchange/searchBook.html',{'books':books,'zitou':zitou,'kehao':kehao,'switch':switch})

def viewUser(request,user_id):
	user = User.objects.get(pk=user_id)
	books = Book.objects.filter(user=user).filter(sold=False)
	requests = Request.objects.filter(user=user).filter(bought=False)
	return render_to_response('exchange/viewUser.html',{'user':user,'books':books,'requests':requests})

@csrf_exempt
def createBook(request):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		return HttpResponseRedirect(reverse('exchange.views.login'))

	if not user.contact:
		return render_to_response('exchange/contactForm.html')
	
	if request.POST:
		book_form = BookForm(request.POST)
		if book_form.is_valid():
			book_form=BookForm(data=request.POST)
			book = book_form.save()
			book.user = user
			book.save()
			return HttpResponseRedirect('/')
	book_form = BookForm()
	request_form = RequestForm()
	return render_to_response('exchange/bookForm.html',{'book_form':book_form,'request_form':request_form,'user':user})

def deleteBook(request, book_id):
	try:
		user = User.objects.get(pk=request.session['current_user'])
	except:
		user = ""
	book = Book.objects.get(pk=book_id)
	if user == book.user:
		book.sold = not book.sold
		book.save()
		return HttpResponseRedirect(reverse('exchange.views.index'))
	else:
		return render_to_response('exchange/bi.html')

@csrf_exempt
def createRequest(request):
	user_id = request.session['current_user']
	user = User.objects.get(pk=user_id)
	if request.POST:
		request_form = RequestForm(request.POST)
		if request_form.is_valid():
			request_form=RequestForm(data=request.POST)
			request = request_form.save()
			request.user = user
			request.save()
			return HttpResponseRedirect('/')
	book_form = BookForm()
	request_form = RequestForm()
	return render_to_response('exchange/bookForm.html',{'book_form':book_form,'request_form':request_form,'user':user})

@csrf_exempt
def register(request):
	if request.POST:
		username = request.POST['username']
		try:
			user = User.objects.get(username=username)
			if user:
				return render_to_response('account/register.html',{'duplicate':True})
		except:
			name = request.POST['name']
			if username and name:
				user = User(username=username,name=name)
				user.save()
				request.session['current_user']=user.id
				return HttpResponseRedirect(reverse('exchange.views.index'))
			else:
				return render_to_response('account/register.html',{'empty':True})
	return render_to_response('account/register.html')

@csrf_exempt
def login(request):
	if request.POST:
		username = request.POST['username']
		try:
			user = User.objects.get(username=username)
			request.session['current_user']=user.id
			return HttpResponseRedirect(reverse('exchange.views.index'))
		except:
			pass
	return render_to_response('account/login.html')

def account(request):
	# books = Book.objects.filter()
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		return HttpResponseRedirect(reverse('exchange.views.login'))
	
	books = Book.objects.filter(user=user)
	books_sold = books.filter(sold=True)
	books = books.filter(sold=False)

	requests = Request.objects.filter(user=user)
	requests_bought = requests.filter(bought=True)
	requests = requests.filter(bought=False)
	return render_to_response('account/account.html',{'user':user,'books':books,'books_sold':books_sold,'requests':requests,'requests_bought':requests_bought})

@csrf_exempt
def addContact(request):
	try:
		user_id = request.session['current_user']
		user = User.objects.get(pk=user_id)
	except:
		return render_to_response('exchange/bi.html')

	if request.POST:
		contact = request.POST['contact']
		if contact:
			contact_cur = user.contact
			user.contact = contact
			user.save()
			if contact_cur:
				return HttpResponseRedirect(reverse('exchange.views.account'))
			else:
				return HttpResponseRedirect(reverse('exchange.views.createBook'))
		else:
			return render_to_response('exchange/contactForm.html')
	else:
		return render_to_response('exchange/contactForm.html')


def logout(request):
	request.session.flush()
	return HttpResponseRedirect(reverse('exchange.views.index'))

def share(request,user_id):
	try:
		user = User.objects.get(pk=user_id)
	except:
		return render_to_response('exchange/bi.html')
	books = Book.objects.filter(user=user).filter(sold=False)
	requests = Request.objects.filter(user=user).filter(bought=False)
	return render_to_response('exchange/share.html',{'books':books,'requests':requests,'user':user, 'share':True})
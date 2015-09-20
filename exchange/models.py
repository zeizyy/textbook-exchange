from django.db import models
#time
from django.utils import timezone
import datetime
# Create your models here.
class Request(models.Model):
	zitou = models.CharField(max_length=30)
	kehao = models.CharField(max_length=30)
	name = models.CharField(max_length=300)
	professor = models.CharField(max_length=100,null=True,blank=True)
	user = models.ForeignKey('User',null=True)
	isbn = models.CharField(max_length=100,blank=True,null=True)
	additional = models.CharField(max_length=1000,blank=True)
	pub_date = models.DateTimeField(default=datetime.datetime.today)
	bought = models.BooleanField(default=False)
	count = models.IntegerField(default=0)

	# def __str__(self):
	def __unicode__(self):
		if self.professor:
			return self.zitou.upper()+str(self.kehao)+"("+self.professor+")"+"-"+self.name
		else:
			return self.zitou.upper()+" "+str(self.kehao)+"-"+self.name

	def index_name(self):
		name = self.zitou.upper()+str(self.kehao)+'-'+self.name
		if len(name) > 25:
			return name[:25]+'...'
		else:
			return name

class Book(models.Model):
	zitou = models.CharField(max_length=30)
	kehao = models.CharField(max_length=30)
	name = models.CharField(max_length=300)
	professor = models.CharField(max_length=100,null=True,blank=True)
	price = models.CharField(max_length=30)
	user = models.ForeignKey('User',null=True)
	new = models.CharField(max_length=30)
	isbn = models.CharField(max_length=100,blank=True,null=True)
	additional = models.CharField(max_length=1000,blank=True)
	pub_date = models.DateTimeField(default=datetime.datetime.today)
	sold = models.BooleanField(default=False)
	count = models.IntegerField(default=0)

	# def __str__(self):
	def __unicode__(self):
		if self.professor:
			return self.zitou.upper()+str(self.kehao)+"("+self.professor+")"+"-"+self.name
		else:
			return self.zitou.upper()+" "+str(self.kehao)+"-"+self.name

	def index_name(self):
		name = self.zitou.upper()+str(self.kehao)+'-'+self.name
		if len(name) > 25:
			return name[:25]+'...'
		else:
			return name

class User(models.Model):
	username = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	contact = models.CharField(max_length=100,null=True,blank=True)

	# def __str__(self):
	def __unicode__(self):
		return self.name+"("+self.username+")"
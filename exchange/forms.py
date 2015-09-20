#coding=utf-8 
from django import forms
from exchange.models import Book, Request
from django.forms import EmailInput,Textarea, NumberInput, DateTimeInput, ModelMultipleChoiceField,CheckboxInput, TextInput, PasswordInput

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ['user','sold','count']
		labels = {
			'zitou':('Department'),
			'kehao':('Course#'),
			'name':('Name'),
			'professor':('Professor(optional)'),
			'price':('Price($)'),
			'new':('Condition(1~10)?'),
			'isbn':('ISBN(optional)'),
			'additional':('Additional Info(optional)'),

		}
		widgets = {
			'pub_date':forms.HiddenInput(),
			'zitou':TextInput(attrs={'class':'form-control','placeholder':'eg.COMM','required':'required'}),
			'kehao':TextInput(attrs={'class':'form-control','placeholder':'eg.1800','required':'required'}),
			'name':TextInput(attrs={'class':'form-control','required':'required'}),
			'professor':TextInput(attrs={'class':'form-control'}),
			'price':TextInput(attrs={'class':'form-control','placeholder':'eg.30','required':'required','aria-describedby':'price'}),
			'new':TextInput(attrs={'class':'form-control','placeholder':'eg.5','aria-describedby':'new'}),
			'isbn':TextInput(attrs={'class':'form-control'}),
			'additional':TextInput(attrs={'class':'form-control'}),
		}

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		exclude = ['user','bought','count']
		labels = {
			'zitou':('Department'),
			'kehao':('Course#'),
			'name':('Name'),
			'professor':('Professor(optional)'),
			'isbn':('ISBN(optional)'),
			'additional':('Additional Info(optional)'),

		}
		widgets = {
			'pub_date':forms.HiddenInput(),
			'zitou':TextInput(attrs={'class':'form-control','placeholder':'eg.COMM','required':'required'}),
			'kehao':TextInput(attrs={'class':'form-control','placeholder':'eg.1800','required':'required'}),
			'name':TextInput(attrs={'class':'form-control','required':'required'}),
			'professor':TextInput(attrs={'class':'form-control'}),
			'isbn':TextInput(attrs={'class':'form-control'}),
			'additional':TextInput(attrs={'class':'form-control'}),
		}

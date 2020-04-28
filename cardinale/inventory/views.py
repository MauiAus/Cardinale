from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib	import messages
from .models import *
from .forms import *

# Create your views here.
# Sam

def homepage(request):
	title = 'Cardinale'
	context = {"title":title,}
	return render(request,"home.html",context)

#displaying items#
def display_beverages(request):
	items = Beverage.objects.filter(owner=request.user).all()
	return render(request, 'inventory.html', {'items':items, 'header':'Beverages'})

def display_snacks(request):
	items = Snack.objects.filter(owner=request.user).all()
	return render(request, 'inventory.html', {'items':items, 'header':'Snacks'})

def display_cans(request):
	items = Can.objects.filter(owner=request.user).all()
	return render(request, 'inventory.html', {'items':items, 'header':'Cans'})

#adding items#
@login_required(login_url="login")
def additem(request, prod, displays, headers):
	if request.method == 'POST':
		form = prod(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return redirect(displays)
	else:
		form = prod()
	return render(request, 'add_item.html',{'form':form, 'header':headers})

def add_beverages(request):
	return additem(request, BeverageForm, display_beverages, 'Beverages')

def add_snacks(request):
	return additem(request, SnackForm, display_snacks, 'Snacks')

def add_cans(request):
	return additem(request, CanForm, display_cans, 'Cans')


#deleting items#
def deleteitem(request, id, prod, displays):
	prod.objects.filter(id=id).delete()
	return redirect(displays)

def del_beverages(request, id):
	return deleteitem(request, id, Beverage, display_beverages)

def del_snacks(request, id):
	return deleteitem(request, id, Snack, display_snacks)

def del_cans(request, id):
	return deleteitem(request, id, Can, display_cans)

#editing items#
def edititem(request, id, prod, forms, displays, header):
	item = get_object_or_404(prod,id=id)
	if request.method == 'POST':
		form = forms(request.POST, request.FILES,instance=item)
		if form.is_valid():
			form.save()
			return redirect(displays)
	else:
		form = forms(instance=item)
		return render(request, "edit_item.html",{'form':form, 'item':item, 'header':header})

def edit_beverages(request, id):
	return edititem(request,id, Beverage, BeverageForm, display_beverages, 'Beverages')

def edit_snacks(request, id):
	return edititem(request,id, Snack, SnackForm, display_snacks, 'Snacks')

def edit_cans(request, id):
	return edititem(request,id, Can, CanForm, display_cans, 'Cans')

#account#
def registerpage(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form':form})

def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or password is invalid')
	context = {}
	return render(request,"login.html",context)

def logoutuser(request):
	logout(request)
	return redirect('home')

"""


def deleteitem(request, id):
	Product.objects.filter(id=id).delete()
	return redirect('display')

def edititem(request, id):
	item = get_object_or_404(Product,id=id)
	if request.method == 'POST':
		form = ProductCreateForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('display')
	else:
		form = ProductCreateForm(instance=item)
		return render(request, "edit_item.html",{'form':form})


"""

"""
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			auth_login(request.POST)
			return redirect('display')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})
"""

import requests
from django.conf import settings
from .models import GroceryUpload
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import GroceryForm
from django.views.generic import View
from django.utils.decorators import method_decorator
# Create your views here.
@login_required(login_url='handleLogin')
def main(request):
    data = GroceryUpload.objects.all()
    return render(request, 'myapp/main.html',{'data':data})
def index(request):
    return render(request, 'myapp/index.html')
@login_required(login_url='handleLogin')
def add(request):
    if request.method == 'POST':
        grocery_upload = GroceryUpload()
        grocery_upload.itemname = request.POST['itemname']
        grocery_upload.itemquantity = request.POST['itemquantity']
        grocery_upload.status = request.POST['status']
        grocery_upload.date = request.POST['date']
        grocery_upload.uploadedby = request.user.username
        grocery_upload.save()
        return redirect('main')
    return render(request, 'myapp/add.html')

# @login_required(login_url='handleLogin')
# def update(request):
#     return render(request, 'myapp/update.html')
@method_decorator(login_required, name='dispatch')
class EditView(View):
  def get(self, request,id):
    groceryUpload = GroceryUpload.objects.get(id=id)
    fm = GroceryForm(instance=groceryUpload)
    return render(request,'myapp/update.html',{'form':fm})
  
  def post(self, request,id):
    groceryUpload = GroceryUpload.objects.get(id=id)
    form = GroceryForm(request.POST,instance=groceryUpload)
    if form.is_valid():
      form.save()
    else:
      print('Reached here')
    return redirect("/main")
@method_decorator(login_required, name='dispatch')
class DeleteView(View):
  def post(self, request,id):
    if request.method == 'POST':
        GroceryUpload.objects.filter(id=id).delete()
    return redirect('/main')
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('handleLogin')

    return render(request, 'myapp/login.html')
def handleLogout(request):
    logout(request)
    messages.info(request,'Successfully logged out')
    return redirect('index')

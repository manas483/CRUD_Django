from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,'insert.html')
def Insertdata(request):
    # data come from html to view
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    # creating object of model class
    # Insertin data into table
    
    newuser = Students.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)


    # After insert render on Show page view
    return redirect('showpage')  # 'showpage' the name of the urls.py

def ShowView(request):
    # Select * From table name
    # Django ORM Quary
    # For fetching all the data of the table
    all_data= Students.objects.all()
    return render(request,'show.html',{'key1':all_data})

# Edit Page View
def EditPage(request,pk):
    # Fetching the data of particular ID
    get_data= Students.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})


# Update data

def Updatedata(request,pk):
    udata= Students.objects.get(id=pk)
    udata.Firstname=request.POST['fname']   # 'Firstname is the coloumn name & 'fname is the name comes from edit.html'
    udata.Lastname=request.POST['lname']   # 'Lastname is the coloumn name & 'lname is the name comes from edit.html'
    udata.Email=request.POST['email']   # 'Email is the coloumn name & 'email is the name comes from edit.html'
    udata.Contact=request.POST['contact']   # 'Contact is the coloumn name & 'contact is the name comes from edit.html'
    # Quary for update
    udata.save()
    # Render to show page
    return redirect('showpage') # 'showpage' the name of the urls

# Delete Data
def DeleteData(request,pk):
    ddata=Students.objects.get(id=pk)
    # Quary for delete
    ddata.delete()
    return redirect('showpage')

def home(request):
    return render(request,'home.html')
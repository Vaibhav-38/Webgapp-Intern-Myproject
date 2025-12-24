from django.shortcuts import render
from .models import Form
# Create your views here.

def index(request):
    return render(request,'index.html')
def form(request):
    if request.method == 'POST':
        name=request.POST.get('name',False)
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        fathername=request.POST.get('fathername')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        city=request.POST.get('city')
        address=request.POST.get('address')
        Form.objects.create(name=name,age=age,dob=dob,fathername=fathername,mobile=mobile,email=email,password=password,city=city,address=address)        
    return render(request,'form.html')
def about(request):
    return render(request,'about.html')
def signup(request):
    return render(request,'sign_up.html')
def signin(request):
    return render(request,'sign_in.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')
def display(request):
    result=Form.objects.all()
    return render(request,'display.html',{"result":result})
def edit(request):
    return render(request,'edit.html')
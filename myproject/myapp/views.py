from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def form(request):
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

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def careers(request):
    return render(request,'careers.html')
def about(request):
    return render(request,'aboutus.html')
def service(request):
    return render(request,'services.html')
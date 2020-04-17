from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request,'services2.html')
def vlsidesign(request):
    return render(request,'vlsidesign.html')
def soc(request):
    return render(request,'soc.html')
def phy(request):
    return render(request,'phy.html')
def fgpa(request):
    return render(request,'fgpa.html')
def esystem(request):
    return render(request,'esystem.html')
def hcircuit(request):
    return render(request,'hcircuit.html')
def firmware(request):
    return render(request,'firmware.html')
def bsp(request):
    return render(request,'bsp.html')
def product(request):
    return render(request,'product.html')
def cloud(request):
    return render(request,'cloud.html')
from django.shortcuts import render
from products.models import Product



def index(request):
    context = {'products' : Product.objects.all()}
    return render(request , 'home/index.html' , context)

def about(request):
    return render(request,'about/about.html')

def contact_us(request):
    return render(request,'contact/contact-us.html')

def blogs(request):
    return render(request,'blog/blogs.html')

def blog(request):
    return render(request,'blog/blog.html')

def terms(request):
    return render(request, 'terms/terms.html')

def error(request):
    return render(request,'404/404.html')

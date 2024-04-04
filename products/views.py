from pydoc import render_doc
from tkinter import E
from django.shortcuts import render
from products.models import Product




def products(request):
    return render(request,'product/products.html',{'products': products})
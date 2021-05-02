from django.shortcuts import render

from .models import Product
from .forms import ProductForm

def product_create_view(request):
    #print(request.GET)
    #print(request.POST)
    if request.method == 'POST':
        new_title=request.POST.get('title')
        print(new_title)
        #Product.objects.create(title=new_title)
    context= {}
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context= {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'summary': obj.summary,
    #     'featured': obj.featured
    # }
    context= {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product
# Create your views here.

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#      if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#        'form': form
#    }
#    return render(request, "product/product_create.html", context)

@login_required(login_url='/login/')
def product_detail_view(request):
    obj = Product.objects.all()
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "product/product_detail.html", context)


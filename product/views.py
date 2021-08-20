from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from rest_framework import viewsets
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from product.models import Product
from .serializers import ProductSerializer
from .forms import ProductForm
from django_filters.views import FilterView
from .filters import ProductFilter


class ProductListView(FilterView):
    filterset_class = ProductFilter
    queryset = Product.objects.filter()
    template_name = 'product.html'
    paginate_by = 20


class ProductCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new product, mixin used to display message
    model = Product  # setting 'Product' model as model
    form_class = ProductForm  # setting 'ProductForm' form as form
    template_name = "edit_product.html"  # 'edit_product.html' used as the template
    success_url = 'product'  # redirects to 'product' page in the url after submitting the form
    success_message = "Product has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Product'
        context["savebtn"] = 'Add to Product'
        return context


class ProductUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit product, mixin used to display message
    model = Product  # setting 'Product' model as model
    form_class = ProductForm  # setting 'ProductForm' form as form
    template_name = "edit_product.html"  # 'edit_product.html' used as the template
    success_url = 'product'  # redirects to 'product' page in the url after submitting the form
    success_message = "Product has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Product'
        context["savebtn"] = 'Update Product'
        context["delbtn"] = 'Delete Product'
        return context


class ProductDeleteView(View):  # view class to delete product
    template_name = "delete_product.html"  # 'delete_product.html' used as the template
    success_message = "Product has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'object': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_deleted = True
        product.save()
        messages.success(request, self.success_message)
        return redirect('product')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer



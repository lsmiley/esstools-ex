from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from rest_framework import viewsets
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from product.models import Category
from .serializers import CategorySerializer
from .forms import CategoryForm
from django_filters.views import FilterView
from .filters import CategoryFilter


class CategoryListView(FilterView):
    filterset_class = CategoryFilter
    queryset = Category.objects.filter()
    template_name = 'category.html'
    paginate_by = 20


class CategoryCreateView(SuccessMessageMixin, CreateView):  # createview class to add new category, mixin used to display message
    model = Category  # setting 'Category' model as model
    form_class = CategoryForm  # setting 'CategoryForm' form as form
    template_name = "edit_category.html"  # 'edit_category.html' used as the template
    success_url = '/category'  # redirects to 'category' page in the url after submitting the form
    success_message = "Category has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Category'
        context["savebtn"] = 'Add to Category'
        return context


class CategoryUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit category, mixin used to display message
    model = Category  # setting 'Category' model as model
    form_class = CategoryForm  # setting 'CategoryForm' form as form
    template_name = "edit_category.html"  # 'edit_category.html' used as the template
    success_url = '/category'  # redirects to 'category' page in the url after submitting the form
    success_message = "Category has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Category'
        context["savebtn"] = 'Update Category'
        context["delbtn"] = 'Delete Category'
        return context


class CategoryDeleteView(View):  # view class to delete category
    template_name = "delete_category.html"  # 'delete_category.html' used as the template
    success_message = "Category has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return render(request, self.template_name, {'object': category})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.is_deleted = True
        category.save()
        messages.success(request, self.success_message)
        return redirect('category')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

# Create your views here.

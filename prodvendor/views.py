from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from product.models import Prodvendor
from .forms import ProdvendorForm
from django_filters.views import FilterView
from .filters import ProdvendorFilter


class ProdvendorListView(FilterView):
    filterset_class = ProdvendorFilter
    queryset = Prodvendor.objects.filter()
    template_name = 'prodvendor.html'
    paginate_by = 10


class ProdvendorCreateView(SuccessMessageMixin, CreateView):  # createview class to add new prodvendor, mixin used to display message
    model = Prodvendor  # setting 'Prodvendor' model as model
    form_class = ProdvendorForm  # setting 'ProdvendorForm' form as form
    template_name = "edit_prodvendor.html"  # 'edit_prodvendor.html' used as the template
    success_url = '/prodvendor'  # redirects to 'prodvendor' page in the url after submitting the form
    success_message = "Prodvendor has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Prodvendor'
        context["savebtn"] = 'Add to Prodvendor'
        return context


class ProdvendorUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit prodvendor, mixin used to display message
    model = Prodvendor  # setting 'Prodvendor' model as model
    form_class = ProdvendorForm  # setting 'ProdvendorForm' form as form
    template_name = "edit_prodvendor.html"  # 'edit_prodvendor.html' used as the template
    success_url = '/prodvendor'  # redirects to 'prodvendor' page in the url after submitting the form
    success_message = "Prodvendor has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Prodvendor'
        context["savebtn"] = 'Update Prodvendor'
        context["delbtn"] = 'Delete Prodvendor'
        return context


class ProdvendorDeleteView(View):  # view class to delete prodvendor
    template_name = "delete_prodvendor.html"  # 'delete_prodvendor.html' used as the template
    success_message = "Prodvendor has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        prodvendor = get_object_or_404(Prodvendor, pk=pk)
        return render(request, self.template_name, {'object': prodvendor})

    def post(self, request, pk):
        prodvendor = get_object_or_404(Prodvendor, pk=pk)
        prodvendor.is_deleted = True
        prodvendor.save()
        messages.success(request, self.success_message)
        return redirect('prodvendor')

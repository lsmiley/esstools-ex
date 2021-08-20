from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from labordelivery.models import Labordelivery
from .forms import LabordeliveryForm
from django_filters.views import FilterView
from .filters import LabordeliveryFilter


class LabordeliveryListView(FilterView):
    filterset_class = LabordeliveryFilter
    queryset = Labordelivery.objects.filter()
    template_name = 'labordelivery.html'
    paginate_by = 20


class LabordeliveryCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new labordelivery, mixin used to display message
    model = Labordelivery  # setting 'Labordelivery' model as model
    form_class = LabordeliveryForm  # setting 'LabordeliveryForm' form as form
    template_name = "edit_labordelivery.html"  # 'edit_labordelivery.html' used as the template
    success_url = '/labordelivery'  # redirects to 'labordelivery' page in the url after submitting the form
    success_message = "Labordelivery has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Labordelivery'
        context["savebtn"] = 'Add to Labordelivery'
        return context


class LabordeliveryUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit labordelivery, mixin used to display message
    model = Labordelivery  # setting 'Labordelivery' model as model
    form_class = LabordeliveryForm  # setting 'LabordeliveryForm' form as form
    template_name = "edit_labordelivery.html"  # 'edit_labordelivery.html' used as the template
    success_url = '/labordelivery'  # redirects to 'labordelivery' page in the url after submitting the form
    success_message = "Labordelivery has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Labordelivery'
        context["savebtn"] = 'Update Labordelivery'
        context["delbtn"] = 'Delete Labordelivery'
        return context


class LabordeliveryDeleteView(View):  # view class to delete labordelivery
    template_name = "delete_labordelivery.html"  # 'delete_labordelivery.html' used as the template
    success_message = "Labordelivery has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        labordelivery = get_object_or_404(Labordelivery, pk=pk)
        return render(request, self.template_name, {'object': labordelivery})

    def post(self, request, pk):
        labordelivery = get_object_or_404(Labordelivery, pk=pk)
        labordelivery.is_deleted = True
        labordelivery.save()
        messages.success(request, self.success_message)
        return redirect('labordelivery')
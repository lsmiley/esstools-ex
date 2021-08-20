from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Configmaster
from .forms import ConfigmasterForm
from django_filters.views import FilterView
from .filters import ConfigmasterFilter


class ConfigmasterListView(FilterView):
    filterset_class = ConfigmasterFilter
    queryset = Configmaster.objects.filter()
    template_name = 'configmaster.html'
    paginate_by = 20


class ConfigmasterCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new configmaster, mixin used to display message
    model = Configmaster  # setting 'Configmaster' model as model
    form_class = ConfigmasterForm  # setting 'ConfigmasterForm' form as form
    template_name = "edit_configmaster.html"  # 'edit_configmaster.html' used as the template
    success_url = '/configmaster'  # redirects to 'configmaster' page in the url after submitting the form
    success_message = "Configmaster has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Configmaster'
        context["savebtn"] = 'Add to Configmaster'
        return context


class ConfigmasterUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit configmaster, mixin used to display message
    model = Configmaster  # setting 'Configmaster' model as model
    form_class = ConfigmasterForm  # setting 'ConfigmasterForm' form as form
    template_name = "edit_configmaster.html"  # 'edit_configmaster.html' used as the template
    success_url = '/configmaster'  # redirects to 'configmaster' page in the url after submitting the form
    success_message = "Configmaster has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Configmaster'
        context["savebtn"] = 'Update Configmaster'
        context["delbtn"] = 'Delete Configmaster'
        return context


class ConfigmasterDeleteView(View):  # view class to delete configmaster
    template_name = "delete_configmaster.html"  # 'delete_configmaster.html' used as the template
    success_message = "Configmaster has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        configmaster = get_object_or_404(Configmaster, pk=pk)
        return render(request, self.template_name, {'object': configmaster})

    def post(self, request, pk):
        configmaster = get_object_or_404(Configmaster, pk=pk)
        configmaster.is_deleted = True
        configmaster.save()
        messages.success(request, self.success_message)
        return redirect('configmaster')
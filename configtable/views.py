from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Configtable
from .forms import ConfigtableForm
from django_filters.views import FilterView
from .filters import ConfigtableFilter


class ConfigtableListView(FilterView):
    filterset_class = ConfigtableFilter
    queryset = Configtable.objects.filter()
    template_name = 'configtable.html'
    paginate_by = 20


class ConfigtableCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new configtable, mixin used to display message
    model = Configtable  # setting 'Configtable' model as model
    form_class = ConfigtableForm  # setting 'ConfigtableForm' form as form
    template_name = "edit_configtable.html"  # 'edit_configtable.html' used as the template
    success_url = '/configtable'  # redirects to 'configtable' page in the url after submitting the form
    success_message = "Configtable has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Configtable'
        context["savebtn"] = 'Add to Configtable'
        return context


class ConfigtableUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit configtable, mixin used to display message
    model = Configtable  # setting 'Configtable' model as model
    form_class = ConfigtableForm  # setting 'ConfigtableForm' form as form
    template_name = "edit_configtable.html"  # 'edit_configtable.html' used as the template
    success_url = '/configtable'  # redirects to 'configtable' page in the url after submitting the form
    success_message = "Configtable has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Configtable'
        context["savebtn"] = 'Update Configtable'
        context["delbtn"] = 'Delete Configtable'
        return context


class ConfigtableDeleteView(View):  # view class to delete configtable
    template_name = "delete_configtable.html"  # 'delete_configtable.html' used as the template
    success_message = "Configtable has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        configtable = get_object_or_404(Configtable, pk=pk)
        return render(request, self.template_name, {'object': configtable})

    def post(self, request, pk):
        configtable = get_object_or_404(Configtable, pk=pk)
        configtable.is_deleted = True
        configtable.save()
        messages.success(request, self.success_message)
        return redirect('configtable')
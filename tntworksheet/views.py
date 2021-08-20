from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Tntworksheet
from .forms import TntworksheetForm
from django_filters.views import FilterView
from .filters import TntworksheetFilter


class TntworksheetListView(FilterView):
    filterset_class = TntworksheetFilter
    queryset = Tntworksheet.objects.filter()
    template_name = 'tntworksheet.html'
    paginate_by = 10


class TntworksheetCreateView(SuccessMessageMixin, CreateView):  # createview class to add new tntworksheet, mixin used to display message
    model = Tntworksheet  # setting 'Tntworksheet' model as model
    form_class = TntworksheetForm  # setting 'TntworksheetForm' form as form
    template_name = "edit_tntworksheet.html"  # 'edit_tntworksheet.html' used as the template
    success_url = '/tntworksheet'  # redirects to 'tntworksheet' page in the url after submitting the form
    success_message = "Tntworksheet has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Tntworksheet'
        context["savebtn"] = 'Add to Tntworksheet'
        return context


class TntworksheetUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit tntworksheet, mixin used to display message
    model = Tntworksheet  # setting 'Tntworksheet' model as model
    form_class = TntworksheetForm  # setting 'TntworksheetForm' form as form
    template_name = "edit_tntworksheet.html"  # 'edit_tntworksheet.html' used as the template
    success_url = '/tntworksheet'  # redirects to 'tntworksheet' page in the url after submitting the form
    success_message = "Tntworksheet has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Tntworksheet'
        context["savebtn"] = 'Update Tntworksheet'
        context["delbtn"] = 'Delete Tntworksheet'
        return context


class TntworksheetDeleteView(View):  # view class to delete tntworksheet
    template_name = "delete_tntworksheet.html"  # 'delete_tntworksheet.html' used as the template
    success_message = "Tntworksheet has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        tntworksheet = get_object_or_404(Tntworksheet, pk=pk)
        return render(request, self.template_name, {'object': tntworksheet})

    def post(self, request, pk):
        tntworksheet = get_object_or_404(Tntworksheet, pk=pk)
        tntworksheet.is_deleted = True
        tntworksheet.save()
        messages.success(request, self.success_message)
        return redirect('tntworksheet')

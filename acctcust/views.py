from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
# from rest_framework import viewsets
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Acctcust
from .serializers import AcctcustSerializer
from .forms import AcctcustForm
from django_filters.views import FilterView
from .filters import AcctcustFilter

# Create your views here.




 # ********  Acctcust Section  ***********

class AcctcustListView(FilterView):
    filterset_class = AcctcustFilter
    queryset = Acctcust.objects.filter()
    template_name = 'acctcust.html'
    paginate_by = 10




class AcctcustCreateView(SuccessMessageMixin, CreateView):  # createview class to add new acctcust, mixin used to display message
    model = Acctcust  # setting 'Acctcust' model as model
    form_class = AcctcustForm  # setting 'AcctcustForm' form as form
    template_name = "edit_acctcust.html"  # 'edit_acctcust.html' used as the template
    success_url = '/acctcust'  # redirects to 'acctcust' page in the url after submitting the form
    success_message = "Acctcust has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Acctcust'
        context["savebtn"] = 'Add to Acctcust'
        return context


class AcctcustUpdateView(SuccessMessageMixin,
                           UpdateView):  # updateview class to edit acctcust, mixin used to display message
    model = Acctcust  # setting 'Acctcust' model as model
    form_class = AcctcustForm  # setting 'AcctcustForm' form as form
    template_name = "edit_acctcust.html"  # 'edit_acctcust.html' used as the template
    success_url = '/acctcust'  # redirects to 'acctcust' page in the url after submitting the form
    success_message = "Acctcust has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Acctcust'
        context["savebtn"] = 'Update Acctcust'
        context["delbtn"] = 'Delete Acctcust'
        return context


class AcctcustDeleteView(View):  # view class to delete acctcust
    template_name = "delete_acctcust.html"  # 'delete_acctcust.html' used as the template
    success_message = "Acctcust has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        acctcust = get_object_or_404(Acctcust, pk=pk)
        return render(request, self.template_name, {'object': acctcust})

    def post(self, request, pk):
        acctcust = get_object_or_404(Acctcust, pk=pk)
        acctcust.is_deleted = True
        acctcust.save()
        messages.success(request, self.success_message)
        return redirect('acctcust')
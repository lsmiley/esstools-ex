from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Labordeliverytype
from .forms import LabordeliverytypeForm
from django_filters.views import FilterView
from .filters import LabordeliverytypeFilter


class LabordeliverytypeListView(FilterView):
    filterset_class = LabordeliverytypeFilter
    queryset = Labordeliverytype.objects.filter()
    template_name = 'labordeliverytype.html'
    paginate_by = 20


class LabordeliverytypeCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new labordeliverytype, mixin used to display message
    model = Labordeliverytype  # setting 'Labordeliverytype' model as model
    form_class = LabordeliverytypeForm  # setting 'LabordeliverytypeForm' form as form
    template_name = "edit_labordeliverytype.html"  # 'edit_labordeliverytype.html' used as the template
    success_url = '/labordeliverytype'  # redirects to 'labordeliverytype' page in the url after submitting the form
    success_message = "Labordeliverytype has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Labordeliverytype'
        context["savebtn"] = 'Add to Labordeliverytype'
        return context


class LabordeliverytypeUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit labordeliverytype, mixin used to display message
    model = Labordeliverytype  # setting 'Labordeliverytype' model as model
    form_class = LabordeliverytypeForm  # setting 'LabordeliverytypeForm' form as form
    template_name = "edit_labordeliverytype.html"  # 'edit_labordeliverytype.html' used as the template
    success_url = '/labordeliverytype'  # redirects to 'labordeliverytype' page in the url after submitting the form
    success_message = "Labordeliverytype has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Labordeliverytype'
        context["savebtn"] = 'Update Labordeliverytype'
        context["delbtn"] = 'Delete Labordeliverytype'
        return context


class LabordeliverytypeDeleteView(View):  # view class to delete labordeliverytype
    template_name = "delete_labordeliverytype.html"  # 'delete_labordeliverytype.html' used as the template
    success_message = "Labordeliverytype has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        labordeliverytype = get_object_or_404(Labordeliverytype, pk=pk)
        return render(request, self.template_name, {'object': labordeliverytype})

    def post(self, request, pk):
        labordeliverytype = get_object_or_404(Labordeliverytype, pk=pk)
        labordeliverytype.is_deleted = True
        labordeliverytype.save()
        messages.success(request, self.success_message)
        return redirect('labordeliverytype')

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Statusstate
from .forms import StatusstateForm
from django_filters.views import FilterView
from .filters import StatusstateFilter


class StatusstateListView(FilterView):
    filterset_class = StatusstateFilter
    queryset = Statusstate.objects.filter()
    template_name = 'statusstate.html'
    paginate_by = 10


class StatusstateCreateView(SuccessMessageMixin, CreateView):  # createview class to add new statusstate, mixin used to display message
    model = Statusstate  # setting 'Statusstate' model as model
    form_class = StatusstateForm  # setting 'StatusstateForm' form as form
    template_name = "edit_statusstate.html"  # 'edit_statusstate.html' used as the template
    success_url = '/statusstate'  # redirects to 'statusstate' page in the url after submitting the form
    success_message = "Statusstate has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Statusstate'
        context["savebtn"] = 'Add to Statusstate'
        return context


class StatusstateUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit statusstate, mixin used to display message
    model = Statusstate  # setting 'Statusstate' model as model
    form_class = StatusstateForm  # setting 'StatusstateForm' form as form
    template_name = "edit_statusstate.html"  # 'edit_statusstate.html' used as the template
    success_url = '/statusstate'  # redirects to 'statusstate' page in the url after submitting the form
    success_message = "Statusstate has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Statusstate'
        context["savebtn"] = 'Update Statusstate'
        context["delbtn"] = 'Delete Statusstate'
        return context


class StatusstateDeleteView(View):  # view class to delete statusstate
    template_name = "delete_statusstate.html"  # 'delete_statusstate.html' used as the template
    success_message = "Statusstate has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        statusstate = get_object_or_404(Statusstate, pk=pk)
        return render(request, self.template_name, {'object': statusstate})

    def post(self, request, pk):
        statusstate = get_object_or_404(Statusstate, pk=pk)
        statusstate.is_deleted = True
        statusstate.save()
        messages.success(request, self.success_message)
        return redirect('statusstate')

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ConfigmasterListView.as_view(), name='configmaster'),
    path('new', views.ConfigmasterCreateView.as_view(), name='new-configmaster'),
    path('configmaster/<pk>/edit', views.ConfigmasterUpdateView.as_view(), name='edit-configmaster'),
    path('configmaster/<pk>/delete', views.ConfigmasterDeleteView.as_view(), name='delete-configmaster'),
]

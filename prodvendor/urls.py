from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProdvendorListView.as_view(), name='prodvendor'),
    path('new', views.ProdvendorCreateView.as_view(), name='new-prodvendor'),
    path('prodvendor/<pk>/edit', views.ProdvendorUpdateView.as_view(), name='edit-prodvendor'),
    path('prodvendor/<pk>/delete', views.ProdvendorDeleteView.as_view(), name='delete-prodvendor'),
]

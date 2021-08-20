from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [

    path('product/', views.ProductListView.as_view(), name='product'),
    path('product/new', views.ProductCreateView.as_view(), name='new-product'),
    path('product/<pk>/edit', views.ProductUpdateView.as_view(), name='edit-product'),
    path('product/<pk>/delete', views.ProductDeleteView.as_view(), name='delete-product'),

]

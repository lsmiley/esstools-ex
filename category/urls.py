from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.CategoryListView.as_view(), name='category'),
    path('category/new', views.CategoryCreateView.as_view(), name='new-category'),
    path('category/<pk>/edit', views.CategoryUpdateView.as_view(), name='edit-category'),
    path('category/<pk>/delete', views.CategoryDeleteView.as_view(), name='delete-category'),
]

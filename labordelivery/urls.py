from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LabordeliveryListView.as_view(), name='labordelivery'),
    path('new', views.LabordeliveryCreateView.as_view(), name='new-labordelivery'),
    path('labordelivery/<pk>/edit', views.LabordeliveryUpdateView.as_view(), name='edit-labordelivery'),
    path('labordelivery/<pk>/delete', views.LabordeliveryDeleteView.as_view(), name='delete-labordelivery'),
]

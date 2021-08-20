from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LabordeliverytypeListView.as_view(), name='labordeliverytype'),
    path('new', views.LabordeliverytypeCreateView.as_view(), name='new-labordeliverytype'),
    path('labordeliverytype/<pk>/edit', views.LabordeliverytypeUpdateView.as_view(), name='edit-labordeliverytype'),
    path('labordeliverytype/<pk>/delete', views.LabordeliverytypeDeleteView.as_view(), name='delete-labordeliverytype'),
]

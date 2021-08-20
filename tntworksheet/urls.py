from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TntworksheetListView.as_view(), name='tntworksheet'),
    path('new', views.TntworksheetCreateView.as_view(), name='new-tntworksheet'),
    path('tntworksheet/<pk>/edit', views.TntworksheetUpdateView.as_view(), name='edit-tntworksheet'),
    path('tntworksheet/<pk>/delete', views.TntworksheetDeleteView.as_view(), name='delete-tntworksheet'),
]

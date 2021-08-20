from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ConfigtableListView.as_view(), name='configtable'),
    path('new', views.ConfigtableCreateView.as_view(), name='new-configtable'),
    path('configtable/<pk>/edit', views.ConfigtableUpdateView.as_view(), name='edit-configtable'),
    path('configtable/<pk>/delete', views.ConfigtableDeleteView.as_view(), name='delete-configtable'),
]

from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StatusstateListView.as_view(), name='statusstate'),
    path('new', views.StatusstateCreateView.as_view(), name='new-statusstate'),
    path('statusstate/<pk>/edit', views.StatusstateUpdateView.as_view(), name='edit-statusstate'),
    path('statusstate/<pk>/delete', views.StatusstateDeleteView.as_view(), name='delete-statusstate'),
]

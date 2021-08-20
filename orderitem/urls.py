from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views
from order.views import (OrderUpdateView)

urlpatterns = [
    path('', views.OrderItemListView.as_view(), name='orderitem'),
    path('new', views.OrderItemCreateView.as_view(), name='new-orderitem'),
    path('orderitem/<pk>/edit', views.OrderItemUpdateView.as_view(), name='edit-orderitem'),
    path('orderitem/<pk>/delete', views.OrderItemDeleteView.as_view(), name='delete-orderitem'),

    # path('update2/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
]

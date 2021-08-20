from django.urls import path
# from django.conf.urls import url
from django.urls import path, include
from . import views
# from sizing.views import (HomepageView, SizingUpdateView, CreateSizingView, delete_sizing,
#                          SizingListView, done_sizing_view, auto_create_sizing_view,
#                          ajax_add_avproduct, ajax_modify_sizingdetail_item, ajax_search_avproducts, ajax_calculate_results_view,
#                          sizing_action_view, ajax_calculate_prodcategory_view
#                          )


urlpatterns = [

    path('', views.AcctcustListView.as_view(), name='acctcust'),
    path('new', views.AcctcustCreateView.as_view(), name='new-acctcust'),
    path('acctcust/<pk>/edit', views.AcctcustUpdateView.as_view(), name='edit-acctcust'),
    path('acctcust/<pk>/delete', views.AcctcustDeleteView.as_view(), name='delete-acctcust'),



]
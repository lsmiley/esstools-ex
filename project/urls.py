from django.conf import settings
# from django.conf.urls import include, url
from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

# from welcome.views import index, health

from order.views import (HomepageView, OrderUpdateView, CreateOrderView, GboUpdateView, delete_order,
                         OrderListView, done_order_view, auto_create_order_view,
                         ajax_add_product, ajax_modify_order_item, ajax_search_products, ajax_calculate_results_view,
                         order_action_view, ajax_calculate_category_view, OrderItemUpdateView, ajax_get_products
                         )


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # path('', include('adminlte_full.urls')),
    # path('', index),
    # path('health', health),
    # path(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),

    # Apps
    path('acctcust/', include('acctcust.urls')),
    path('labordeliverytype/', include('labordeliverytype.urls')),
    path('labordelivery/', include('labordelivery.urls')),
    path('tntworksheet/', include('tntworksheet.urls')),
    path('statusstate/', include('statusstate.urls')),
    path('prodvendor/', include('prodvendor.urls')),
    path('orderitem/', include('orderitem.urls')),

    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('', HomepageView.as_view(), name='homepage'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('create-auto/', auto_create_order_view, name='create_auto'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('updategbo/<int:pk>/', GboUpdateView.as_view(), name='update_gbo'),
    path('gbo/<int:pk>/', GboUpdateView.as_view(), name='gbo'),
    path('updateitem/<int:pk>/', OrderItemUpdateView.as_view(), name='update_orderitem'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('orderitem/orderitem/<pk>/edit', OrderItemUpdateView.as_view(), name='edit-orderitem'),

    path('done/<int:pk>/', done_order_view, name='done_order'),
    path('delete/<int:pk>/', delete_order, name='delete_order'),
    path('action/<int:pk>/<slug:action>/', order_action_view, name='order_action'),

    # path('edit_orderitem/<int:pk>/', OrderItemEditView.as_view(), name='edit_orderitem'),
    #
    # re_path(r'^ordertitem/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.OrderItemEditView.as_view(),
    #         name='orderitem'),

    # path('orderitem_update/<int:pk>/', OrderItemUpdateView.as_view(), name='orderitem_update'),

    #  ajax_calls
    path('ajax/search-products/<int:pk>/', ajax_search_products, name='ajax-search'),
    path('ajax/add-product/<int:pk>/<int:dk>/', ajax_add_product, name='ajax_add'),
    path('ajax/modify-product/<int:pk>/<slug:action>', ajax_modify_order_item, name='ajax_modify'),
    path('ajax/calculate-results/', ajax_calculate_results_view, name='ajax_calculate_result'),
    path('ajax/calculate-category-results/', ajax_calculate_category_view, name='ajax_category_result'),
    path('ajax-get-products/', ajax_get_products, name="ajax_get_products"),

    #  API_calls
    # path('saveorderitem', saveorderitem, name='saveorderitem'),
    # path('saveorderitem', apiViews.saveorderitem, name='saveorderitem'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
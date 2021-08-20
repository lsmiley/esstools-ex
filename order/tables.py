import django_tables2 as tables

from product.models import Product
from .models import OrderItem, Order


class OrderTable(tables.Table):
    tag_final_value = tables.Column(orderable=False, verbose_name='Value')
    action = tables.TemplateColumn(
        '<a href="{{ record.get_edit_url }}" class="btn btn-info"><i class="fa fa-edit"></i></a>', orderable=False)

    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap.html'
        fields = ['date', 'title', 'tag_final_value']


class ProductTable(tables.Table):
    tag_final_value = tables.Column(orderable=False, verbose_name='Price')
    action = tables.TemplateColumn(
        '<button class="btn btn-info add_button" data-href="{% url "ajax_add" instance.id record.id %}">Add!</a>',
        orderable=False
    )

    class Meta:
        model = Product
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'category', 'tag_final_value']


class OrderItemTable(tables.Table):
    numworkstation = tables.Column(orderable=False, verbose_name='# Wkstn.')
    wkstnshourscalc = tables.Column(orderable=False, verbose_name='Wkstn/Hrs.')
    numserver = tables.Column(orderable=False, verbose_name='# Svrs')
    srvshourscalc = tables.Column(orderable=False, verbose_name='Svr/Hrs.')
    numipaddress = tables.Column(orderable=False, verbose_name='# IP/EP')
    ipshourscalc = tables.Column(orderable=False, verbose_name='IP/Hrs.')
    tag_final_totalhourscalc = tables.Column(orderable=False, verbose_name='Ttl/Hrs.')
    total_endpoints = tables.Column(orderable=False, verbose_name='# Endpoints')
    qty = tables.Column(orderable=False, verbose_name='# Consoles')
    price = tables.Column(orderable=False, verbose_name='Base')
    tag_line_base_hours = tables.Column(orderable=False, verbose_name='Hrs.')

    # tag_final_price = tables.Column(orderable=False, verbose_name='Price')

    Options = tables.TemplateColumn('''
            <div class="btn-group">
            
                                    <button class="btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0"
                                            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        <span class="icon icon-sm">
                                            <span class="fas fa-ellipsis-h icon-dark"></span>
                                        </span>
                                        <span class="sr-only">Toggle Dropdown</span>
                                    </button>
                                    <div class="dropdown-menu">
                                        <a class="dropdown-item edit_item"
                                      
                                            <span class="fas fa-edit mr-2"></span>Edit
                                        </a>
                                        <a class="dropdown-item text-danger delete_item"

                                            <span class="fas fa-trash-alt mr-2"></span>Remove
                                        </a>
            <button data-href="{% url "ajax_modify" record.id "add" %}" class="btn btn-success edit_button"><i class="fa fa-arrow-up"></i></button>
            <button data-href="{% url "ajax_modify" record.id "remove" %}" class="btn btn-warning edit_button"><i class="fa fa-arrow-down"></i></button>
            <button data-href="{% url "ajax_modify" record.id "delete" %}" class="btn btn-danger edit_button"><i class="fa fa-trash"></i></button>
            <span class="btn btn-info btn-sm edit" style="cursor:pointer;" data-toggle="modal" data-target="#modal-Edit"></span>
            <a href="{% url 'orderitem' %}orderitem/{{ record.id }}/edit">Update</a>
            <a class="sidebar-link waves-effect waves-dark sidebar-link" href="{% url 'orderitem' %}" aria-expanded="false"><i class="mdi mdi-border-inside"></i><span class="hide-menu">Sizing Detail</span></a>
            <a href="{% url 'orderitem' %}orderitem/{{ record.id }}/edit" class="btn btn-block btn-info btn-xs">Details</a>
            
            

           
            

           
                                    </div>
                                </div>
    ''', orderable=False)

    class Meta:
        model = OrderItem
        template_name = 'django_tables2/bootstrap.html'
        fields = ['product']

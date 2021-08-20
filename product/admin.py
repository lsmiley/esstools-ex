from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'tag_final_value', 'qty', 'active']
    list_select_related = ['category']
    list_filter = ['active', 'category']
    search_fields = ['title']
    list_per_page = 50
    fields = ['active', 'title', 'value', 'discount_value', 'final_value', 'qty', 'productname', 'productdesc',
              'productnote', 'productcomplexitybase', 'numcomponent', 'primarycomp', 'component1', 'component1desc','componentcomplexityhrs1', 'componentcomplexityfac1',
              'ComponentHours1', 'Component1_Wkstn', 'Component1_Svr', 'Component1_IP', 'Component1_Qty',
              'memocomponent1note', 'component2', 'component2desc', 'componentcomplexityhrs2', 'componentcomplexityfac2', 'ComponentHours2', 'Component2_Wkstn',
              'Component2_Svr', 'Component2_IP', 'Component2_Qty', 'memocomponent2note', 'component3', 'component3desc','componentcomplexityhrs3', 'componentcomplexityfac3',
              'ComponentHours3', 'Component3_Wkstn', 'Component3_Svr', 'Component3_IP', 'Component3_Qty',
              'memocomponent3note', 'component4', 'component4desc', 'componentcomplexityhrs4', 'componentcomplexityfac4', 'ComponentHours4', 'Component4_Wkstn',
              'Component4_Svr', 'Component4_IP', 'Component4_Qty', 'memocomponent4note', 'component5', 'component5desc',
              'componentcomplexityhrs5', 'componentcomplexityfac5', 'ComponentHours5', 'Component5_Wkstn',
              'Component5_Svr', 'Component5_IP', 'Component5_Qty', 'memocomponent5note', 'component6', 'component6desc','componentcomplexityhrs6', 'componentcomplexityfac6',
              'ComponentHours6', 'Component6_Wkstn', 'Component6_Svr', 'Component6_IP', 'Component6_Qty',
              'memocomponent6note', 'component7', 'component7desc', 'componentcomplexityhrs7', 'componentcomplexityfac7', 'ComponentHours7', 'Component7_Wkstn',
              'Component7_Svr', 'Component7_IP', 'Component7_Qty', 'memocomponent7note', 'component8', 'component8desc', 'componentcomplexityhrs8', 'componentcomplexityfac8',
              'ComponentHours8', 'Component8_Wkstn', 'Component8_Svr', 'Component8_IP', 'Component8_Qty',
              'memocomponent8note', 'component9', 'component9desc', 'componentcomplexityhrs9', 'componentcomplexityfac9', 'ComponentHours9', 'Component9_Wkstn',
              'Component9_Svr', 'Component9_IP', 'Component9_Qty', 'memocomponent9note', 'component10',
              'component10desc', 'componentcomplexityhrs10', 'componentcomplexityfac10', 'ComponentHours10', 'Component10_Wkstn', 'Component10_Svr', 'Component10_IP',
              'Component10_Qty', 'memocomponent10note', 'component11', 'component11desc', 'componentcomplexityhrs11', 'componentcomplexityfac11', 'ComponentHours11',
              'Component11_Wkstn', 'Component11_Svr', 'Component11_IP', 'Component11_Qty', 'memocomponent11note',
              'component12', 'component12desc', 'componentcomplexityhrs12', 'componentcomplexityfac12', 'ComponentHours12', 'Component12_Wkstn', 'Component12_Svr',
              'Component12_IP', 'Component12_Qty', 'memocomponent12note', 'component13', 'component13desc', 'componentcomplexityhrs13', 'componentcomplexityfac13',
              'ComponentHours13', 'Component13_Wkstn', 'Component13_Svr', 'Component13_IP', 'Component13_Qty',
              'memocomponent13note', 'component14', 'component14desc', 'componentcomplexityhrs14', 'componentcomplexityfac14', 'ComponentHours14', 'Component14_Wkstn',
              'Component14_Svr', 'Component14_IP', 'Component14_Qty', 'memocomponent14note', 'component15',
              'component15desc', 'componentcomplexityhrs15', 'componentcomplexityfac15', 'ComponentHours15', 'Component15_Wkstn', 'Component15_Svr', 'Component15_IP',
              'Component15_Qty', 'memocomponent15note', 'memoproductnote', 'memotechnicalnote', 'endpoint_ip',
              'prodimage', 'addlconsole', 'prodvendor', 'category']

    autocomplete_fields = ['category']
    readonly_fields = ['tag_final_value']

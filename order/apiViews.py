from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from order.models import Order, OrderItem
from product.models import Product


@csrf_exempt
def getSubjects(request):
    product = Product.objects.filter(product_id=request.POST.get('product_id', ''))
    product_obj = serializers.serialize('product', product)
    return JsonResponse(product_obj, safe=False)

@csrf_exempt
def saveorderitem(request):
    id = request.POST.get('id', '')
    type = request.POST.get('type', '')
    value = request.POST.get('value', '')
    orderitem = OrderItem.objects.get(id=id)
    if type == "numworkstation":
       orderitem.numworkstation = value

    if type == "numserver":
        orderitem.numserver = value

    if type == "numipaddress":
        orderitem.numipaddress = value

    if type == "nummonths":
        orderitem.nummonths = value

    if type == "labordelivery":
        orderitem.labordelivery = value

    orderitem.save()
    return JsonResponse({"success": "Updated"})



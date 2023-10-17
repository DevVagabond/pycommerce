from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer, ProductCreateSerializer


@csrf_exempt
@api_view(["POST"])
def api_home(req):
    data = {}
    serializerData = ProductCreateSerializer(data=req.data)
    if serializerData.is_valid():
        serializerData.save()
        data["success"] = "Product created successfully"
    else:
        data["error"] = serializerData.errors

    return Response(data)


@api_view(["GET"])
def fetchAllProducts(req):
    products = Product.objects().all()
    serializeData = ProductSerializer(products, many=True)
    return Response(serializeData.data)

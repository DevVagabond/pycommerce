from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework import permissions, authentication
from .permissions import IsStaffMember


@api_view(['GET'])
def listProduct(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


class createProduct(generics.CreateAPIView):
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffMember
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class getProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class updateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


createProduct = createProduct.as_view()
getProduct = getProduct.as_view()
updateProduct = updateProduct.as_view()

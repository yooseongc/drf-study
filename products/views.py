from django.core.files.storage import default_storage
from rest_framework import generics, mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from admin.pagination import CustomPagination
from products.models import Product
from products.serializers import ProductSerializer
from users.authentication import JWTAuthentication
from users.permissions import ViewPermissions


class ProductGenericAPIView(generics.GenericAPIView,
                            mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin, mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated & ViewPermissions]
    permission_object = 'products'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({'data': self.retrieve(request, pk).data})
        return self.list(request)

    def post(self, request):
        resp = self.create(request)
        return Response({'data': resp.data}, status=resp.status_code)

    def put(self, request, pk=None):
        resp = self.partial_update(request, pk)
        return Response({'data': resp.data}, status=resp.status_code)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class FileUploadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.FILES['image']
        file_name = default_storage.save(file.name, file)
        media_url = default_storage.url(file_name)
        return Response({'url': f"{request.scheme}://{request.get_host()}/api{media_url}"})

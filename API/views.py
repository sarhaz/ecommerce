from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, ProductSerializer, ContactSerializer, CartSerializer, LogoSerializer,  ClientSerializer, CheckoutSerializer
from landing.models import Product, Category, Client, Checkout, Contact, Cart, Logos
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.db.transaction import atomic
from rest_framework import status


class HomeAPIView(APIView):
    def get(self, request):
        return Response(data={'message': 'API!'})


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'category__name')
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def bought(self, request, *args, **kwargs):
        products = self.get_object()
        with atomic():
            products.bought += 1
            products.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def expensive(self, request, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by('-price')[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def cheap(self, request, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by('price')[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def bought(self, request, *args, **kwargs):
        category = self.get_object()
        with atomic():
            category.bought += 1
            category.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def reset_bought(self, request, *args, **kwargs):
        category = self.get_object()
        with atomic():
            category.bought = 0
            category.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def latest_categories(self, request, *args, **kwargs):
        category = self.get_queryset()
        latest_categories = category.order_by('-created_at')[:10]
        serializer = CategorySerializer(latest_categories, many=True)
        return Response(serializer.data)


class ContactAPIView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def new_users(self, request, *args, **kwargs):
        user = self.get_queryset()
        new_users = user.order_by('-created_at')[:10]
        serializer = ContactSerializer(new_users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def is_active(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def seen(self, request, *args, **kwargs):
        user = self.get_queryset()
        with atomic():
            user.seen += 1
            user.save()
            return Response(status=status.HTTP_200_OK)


class LogosAPIView(ModelViewSet):
    queryset = Logos.objects.all()
    serializer_class = LogoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('image', )
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def url_image(self, request, *args, **kwargs):
        image = self.get_object()
        return Response(data={'image': image.url}, status=status.HTTP_200_OK)


class ClientAPIView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def new_users(self, request, *args, **kwargs):
        user = self.get_queryset()
        new_users = user.order_by('-created_at')[:10]
        serializer = ClientSerializer(new_users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def full_name(self, request, *args, **kwargs):
        first_name = self.get_object()
        last_name = self.get_object()
        full_name = f"{first_name} {last_name}"
        serializer = ClientSerializer(full_name)
        return Response(serializer.data)


class CheckoutAPIView(ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('total', 'cart')
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def mark_as_shipped(self, request, *args, **kwargs):
        checkout = self.get_object()
        checkout.shipped = True
        checkout.save()
        return Response({'status': 'Checkout marked as shipped'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def mark_as_delivered(self, request, *args, **kwargs):
        checkout = self.get_object()
        checkout.delivered = True
        checkout.save()
        return Response({'status': 'Checkout marked as delivered'}, status=status.HTTP_200_OK)


class CartsAPIView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('product__name', 'quantity', 'total')
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def add_shipping_cost(self, request, *args, **kwargs):
        cart = self.get_object()
        shipping_cost = request.data.get('shipping_cost', 0)
        cart.shipping = shipping_cost
        cart.save()
        return Response({'status': 'Shipping cost added', 'shipping_cost': shipping_cost}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def calculate_total(self, request, *args, **kwargs):
        cart = self.get_object()
        total = cart.total + cart.shipping
        return Response({'total': total}, status=status.HTTP_200_OK)
from django.urls import path, include
from .views import HomeAPIView, CategoryAPIView, CartsAPIView, LogosAPIView, ContactAPIView, ProductAPIView, ClientAPIView, CheckoutAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router = DefaultRouter()
router.register("product", viewset=ProductAPIView)
router.register("category", viewset=CategoryAPIView)
router.register("cart", viewset=CartsAPIView)
router.register("logo", viewset=LogosAPIView)
router.register("client", viewset=ClientAPIView)
router.register("contact", viewset=ContactAPIView)
router.register("checkout", viewset=CheckoutAPIView)

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]

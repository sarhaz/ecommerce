from django.urls import path
from .views import LandingPageView, TshirtsPageView, SneakersPageView, ShopViewAdmin, FavouriteView, ShopView, ShopDetailViewUser, CartView, ContactView, CheckoutView, UpdateProductView, DeleteProductView, ShopDetailViewAdmin, SuccessPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('sneakers/', SneakersPageView.as_view(), name='sneakers'),
    path('T_shirts/', TshirtsPageView.as_view(), name='T_shirts'),
    path('shop/admin', ShopViewAdmin.as_view(), name='shop_admin'),
    path('cart/<int:id>/', CartView.as_view(), name='cart'),
    path('favourites/', FavouriteView.as_view(), name='favourites'),
    path('success/', SuccessPageView.as_view(), name='success'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('update/<int:id>/', UpdateProductView.as_view(), name='update'),
    path('delete/<int:id>/', DeleteProductView.as_view(), name='delete'),
    path('shop_detail/<int:id>/', ShopDetailViewUser.as_view(), name='shop_detail'),
    path('shop_detail/admin/<int:id>/', ShopDetailViewAdmin.as_view(), name='shop_detail_admin'),
]

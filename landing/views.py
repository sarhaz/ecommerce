from msilib.schema import ListView

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Category, Logos, Cart, Checkout, Contact
from django.contrib.auth.mixins import LoginRequiredMixin


class LandingPageView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            categories = Category.objects.all()
            product = Product.objects.all()
            logos = Logos.objects.all()
            context = {
                "categories": categories,
                "logos": logos,
                "search": search,
                "product": product
            }
            return render(request, 'index.html', context)
        else:
            categories = Category.objects.filter(name__icontains=search)
            product = Product.objects.all()
            logos = Logos.objects.all()
            if categories:
                context = {
                    "categories": categories,
                    "logos": logos,
                    "search": search,
                    "product": product
                }
                return render(request, 'index.html', context)
            else:
                context = {
                    "search": search,
                    "logos": logos,
                    "categories": categories,
                    "product": product
                }
                return render(request, 'index.html', context)


class SneakersPageView(View):
    def get(self, request):
        sneakers_category = Category.objects.get(name__icontains='sneakers')
        sneakers = Product.objects.filter(category=sneakers_category)
        context = {
            "sneakers": sneakers
        }
        return render(request, 'sneakers.html', context)


class TshirtsPageView(View):
    def get(self, request):
        T_shirts = Category.objects.all()
        T_shirts = T_shirts.filter(name__icontains='T_shirts')
        context = {
            "T_shirts": T_shirts
        }
        return render(request, 'T_shirts.html', context)


class ShopView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        categories = Category.objects.all()
        if not search:
            products = Product.objects.all()
            context = {
                "products": products,
                "categories": categories,
            }
            return render(request, 'shop.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {
                    "products": products,
                    "categories": categories,
                }
                return render(request, 'shop.html', context)
            else:
                context = {
                    "products": products,
                    "categories": categories,
                }
                return render(request, 'shop.html', context)


class ShopViewAdmin(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        categories = Category.objects.all()
        if not search:
            products = Product.objects.all()
            context = {
                "products": products,
                "categories": categories,
            }
            return render(request, 'shop_admin.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {
                    "products": products,
                    "categories": categories,
                }
                return render(request, 'shop_admin.html', context)
            else:
                context = {
                    "products": products,
                    "categories": categories,
                }
                return render(request, 'shop_admin.html', context)


class ShopDetailViewAdmin(LoginRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {
            "product": product,
        }
        return render(request, 'shop_detail_admin.html', context)


class ShopDetailViewUser(LoginRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        categories = Category.objects.all()
        context = {
            "product": product,
            "categories": categories,
        }
        return render(request, 'shop_detail.html', context)


class CartView(LoginRequiredMixin, View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        cart = Cart.objects.create(user=request.user, products=products)
        cart.save()
        cart = Cart.objects.filter(user=request.user)
        context = {
            "cart": cart
        }
        return render(request, 'cart.html', context)


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        contact = Contact.objects.all()
        categories = Category.objects.all()
        context = {
            "contact": contact,
            "categories": categories,
        }
        return render(request, 'contact.html', context)


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        checkout = Checkout.objects.all()
        products = Product.objects.all()
        categories = Category.objects.all()
        context = {
            "checkout": checkout,
            "products": products,
            "categories": categories,
        }
        return render(request, 'checkout.html', context)

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        zip_code = request.POST['zip_code']
        user = User(zip_code=zip_code, first_name=first_name, last_name=last_name, phone=phone, email=email, address=address, city=city, country=country)
        user.save()
        return redirect('landing')


class UpdateProductView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        categories = Category.objects.all()
        context = {
            "product": product,
            "categories": categories,
        }
        return render(request, 'update_product.html', context)

    def post(self, request, id):
        product = Product.objects.get(id=id)
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.count = request.POST['count']
        product.color = request.POST['color']
        product.size = request.POST['size']
        product.weight = request.POST['weight']

        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.save()
        return redirect("shop")


class DeleteProductView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect("shop")


class SuccessPageView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'success.html', {"categories": categories})


class FavouriteView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        context = {
            "products": products,
            "categories": categories,
        }
        return render(request, 'favourites.html', context)


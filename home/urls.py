"""
URL configuration for mshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

	path('', views.home_page, name='home'),

    path('about_us/', views.about_us, name='about_us'),
    path('brands/', views.brands, name='brands'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),


	
    path('faq/', views.faq, name='faq'),
	path('our_store/', views.our_store,  name='our_store'),
	path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('register/', views.register, name='register'),
    path('store/', views.store, name='store'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),

   

    path('account/', views.account, name='account'),
    path('account_edit/', views.account_edit, name='account_edit'),
    path('account_orders/', views.account_orders, name='account_orders'),
    path('change_password/', views.change_password, name='change_password'),
    path('account_address/', views.account_address, name='account_address'),
    path('account_wishlist/', views.account_wishlist, name='account_wishlist'),
    path('account_orders_details/<int:order_id>/', views.account_orders_details, name='account_orders_details'),


    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:product_id>/', views.add_wishlist, name='add_wishlist'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),

    path('catalog/', views.store, name='catalog'),
    path('catalog/<slug:category_slug>/', views.store, name='products_by_category'),
    path('catalog/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),


    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('payment_complete/', views.payment_complete, name='payment_complete'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),
    path('order_complete/', views.order_complete, name='order_complete'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

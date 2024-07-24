from django.urls import path
from KEYCHAINGE import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/blog', views.blog, name='blog'),
    path('main/cart', views.cart, name='cart'),
    path('main/category', views.category, name='category'),
    path('main/checkout', views.checkout, name='checkout'),
    path('main/confirmation', views.confirmation, name='confirmation'),
    path('main/contact', views.contact, name='contact'),
    path('main/elements', views.elements, name='elements'),
    path('main/feature', views.feature, name='feature'),
    path('main/login', views.login, name='login'),
    path('main/single-blog', views.SingleBlog, name='SingleBlog'),
    path('main/single-product', views.SingleProduct, name='SingleProduct'),
    path('main/head', views.head, name='head'),
    path('main/header', views.header, name='header'),
    path('main/footer', views.footer, name='footer'),
    path('main/tracking', views.tracking, name='tracking'),
]
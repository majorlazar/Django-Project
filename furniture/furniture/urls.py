from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from furniture_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home_about/', views.home_about,name='home_about'),
    path('home_contact/', views.home_contact),
    # path('userhome', views.user_home),
    path('userhome', views.user_home, name='userhome'),
    path('login', views.login),
###
    path('forgot', views.forgot_password, name="forgot"),
    path('reset/<token>', views.reset_password, name='reset_password'),
###
    # path('view_order', views.view_order,name='view_order'),
    path('order_details', views.order_details,name='order_details'),
    path('reorder', views.reorder),
    path('remove_product/<int:id>', views.remove_product,name='remove_product'),
    # path('admin_view_order', views.admin_view_order, name='admin_view_order'),

    path('view_order/', views.view_orders, name='view_order'),
    path('admin_view_order/<int:order_id>/', views.admin_view_order, name='admin_view_order'),
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),

    path('shop', views.shop, name='shop'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


    path('about', views.about),
    path("profile", views.profile, name="profile"),

    path('cart', views.cart_view),

    path('contact', views.contact),
    path('blog', views.blog),
    path('checkout', views.checkout),
    path('adminhome/', views.admin_home),
    path('prod_approval/', views.prod_approval),

    path('register', views.create_user),
    path('logout', views.logout),
    path('view_user/', views.view_user),
    path('addproduct', views.add_product),

    path('prod_approval', views.prod_approval, name='prod_approval'),
    path('update_order_status/<int:order_id>', views.update_order_status),

path('place_order', views.place_order, name='place_order'),
    path('payment_success', views.payment_success, name='payment_success'),

    # path('payment', views.payment),
    path('approve_product/<int:id>', views.approve_product, name='approve_product'),
    path('reject_product/<int:id>', views.reject_product, name='reject_product'),


    path('shop', views.shop),
    path('increase_quantity/<int:item_id>',views.increase_quantity,name='increase_quantity'),
    path('decrease_quantity/<int:item_id>',views.decrease_quantity,name='decrease_quantity'),
    path('remove_item/<int:item_id>',views.remove_item,name='remove_item'),
    path('product_status/', views.product_status, name='product_status'),

]

# ✅ This serves media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from .views import admin_login_view, authenticate_admin, admin_homepage_view, logout_admin, add_pizza, delete_pizza, homepage_view, signup_user, user_login_view, user_welcome_view, authenticate_user, user_logout, place_order, user_orders, admin_order, accept_order, decline_order

urlpatterns = [
    path('admin/', admin_login_view, name='admin_login_page'),
    path('admin_authenticate/', authenticate_admin),
    path('admin/homepage/', admin_homepage_view, name='admin_homepage'),
    path('admin_logout/', logout_admin),
    path('add_pizza/', add_pizza),
    path('delete_pizza/<int:pizza_id>/', delete_pizza),
    path('', homepage_view, name='homepage'),
    path('signup_user/', signup_user),
    path('login_user/', user_login_view, name='user_login_page'),
    path('user_welcome/', user_welcome_view, name='user_page'),
    path('user_login_successful/', authenticate_user),
    path('user_logout/', user_logout),
    path('place_order/', place_order),
    path('user_orders_section/', user_orders),
    path('admin_orders_section/', admin_order),
    path('accept_order/<int:order_id>/', accept_order),
    path('decline_order/<int:order_id>/', decline_order),
]

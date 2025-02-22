from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('registercustomer/', views.customer_register, name='customer_register'),
    path('registerstaf/', views.staf_register, name='staf_register'),
    path('registeradmin/', views.admin_register, name='admin_register'),
    path('registerdeliveryboy/', views.deliveryboy_register, name='deliveryboy_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('customerhome',views.customerhome,name='customerhome'),
    path('deliveryboyhome',views.deliveryboyhome,name='deliveryboyhome'),



]

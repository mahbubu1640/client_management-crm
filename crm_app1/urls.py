from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page_view,name="home"),
    path('register/', views.register_view,name="register"),
    path('logout/', views.logout_view,name="logout"),
    path('create/', views.create_customer,name="create"),
    path('list/', views.list_customer,name="list-customer"),
    path('detail/<int:pk>', views.detail_customer,name="detail"),
    path('update/<int:pk>', views.update_view,name="update"),
]
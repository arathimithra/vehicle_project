from django.urls import path
from . import views
from .views import VehicleList, VehicleUpdate, VehicleCreate

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('list/', VehicleList.as_view(), name='vehicle'),
    path('update/<int:pk>/', VehicleUpdate.as_view(), name='vehicle-update'),
    path('create/', VehicleCreate.as_view(), name='vehicle-create'),
    path('superadminpage/', views.admin, name='superadminpage'),
    path('customer/', views.customer, name='customer'),
    path('admin/', views.employee, name='admin'),
]
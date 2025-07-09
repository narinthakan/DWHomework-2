from django.urls import path
from . import views

urlpatterns = [
    path('', views.hw04_view, name='hw04_view'),  # ใช้ hw04_view เป็นหน้าแรก
    path('hw04/', views.hw04_view, name='hw04_view'),  # path สำหรับ hw04
 
 
 
 
 
 ]
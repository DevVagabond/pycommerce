from django.urls import path, include

from . import views

urlpatterns = [
    path("list", views.listProduct, name="api_home"),
    path("create", views.createProduct, name="createProduct"),
    path("<int:pk>", views.getProduct, name="getProduct"),
    path("<int:pk>/update", views.updateProduct, name="updateProduct"),
]

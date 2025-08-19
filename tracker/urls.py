from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete-transaction/<uuid>/',views.deleteTransaction, name="delete-transaction"),
]

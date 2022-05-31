from django.urls import path
from cart import views

urlpatterns = [
    path('order/', views.BasketApiView.as_view())
]
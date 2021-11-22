from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('details', index),
    path("purchases", index),
    path('profile', index),
]
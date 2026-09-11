from django.urls import path
from .views import jadval, post_royxat

urlpatterns = [
    path('jadval/',jadval, name='jadval'),
    path('post/',post_royxat, name='post'),
]
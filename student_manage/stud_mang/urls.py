from django.urls import path
from .import views

urlpatterns=[
    path('home',views.home),
    path('edit/<a>',views.Edit_std),
    path('delete/<a>',views.Delete),
]
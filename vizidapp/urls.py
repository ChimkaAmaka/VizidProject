from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.room, name='rooms'),
    path('', views.makepayment, name='make payment'),
    path('', views.contact, name='contact'),
    path('comments/', views.Comment, name='comments'),
    path('', views.about, name='about us'),
]
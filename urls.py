from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('allposts/', views.allposts, name='allposts'),
    path('allposts/filter', views.get_Post, name='filter'),
    path('editpost/<int:postid>', views.editpost, name='editpost'),
    path('claimpost/<int:postid>', views.claimpost, name='claimpost'),
]

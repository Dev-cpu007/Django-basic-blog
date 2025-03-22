from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.test),
    path('login/',views.loginn,name = "login"),
    path('signup/',views.signup,name = "signup"),
    path('home/',views.home,name="home"),
    path('newpost/',views.newPost,name="newpost"),
    path('mypost/',views.myPost,name="mypost"),
    path('signout/',views.signout,name = "signout"),
    path('delete/<int:id>/',deletePost,name = "delete_post")
]
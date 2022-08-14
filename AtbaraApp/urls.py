from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login1, name="login"),
    path('upload', views.upload, name="upload"),
    path('youtuber', views.youtuber, name="youtuber"),
]

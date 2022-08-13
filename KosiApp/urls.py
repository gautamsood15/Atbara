from django.urls import path 
from .views import create_channel, channel

urlpatterns = [
    path("channel/create/", create_channel, name="create"),
    path("channel/<slug>/", channel, name="mychannel"),
]
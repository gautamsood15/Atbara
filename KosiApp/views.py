from django.shortcuts import render
from .models import Channel

# Create your views here.


def channel(request, slug):
    mychannel = Channel.objects.get(slug=slug)
    context = {
        "channel": mychannel
    }

    return render(request, "channel/channel_home.html", context)


def create_channel(request):
    pass
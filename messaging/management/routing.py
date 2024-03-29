from django.urls import re_path

from .consumers import ChatConsumer

# Create here
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<group>\w+)/$", ChatConsumer.as_asgi())
]
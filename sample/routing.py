from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .consumer import ServerConsumer
from django.urls import re_path
websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', ServerConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
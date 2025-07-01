import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from realtime.routing import websocket_urlpatterns  # นำเข้า WebSocket routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # ใช้ WebSocket URL routing
        )
    ),
})

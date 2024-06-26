import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import api.routing  # Update with your project name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexfit_django.settings')  # Update with your project name
print("Printing OS envrio Settings")
print(os.environ.get('DJANGO_SETTINGS_MODULE'))

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Initialize Django application for HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.routing.websocket_urlpatterns  # Verify the routing for WebSocket connections
        )
    ),
})
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # For demo: allow any
from rest_framework.response import Response
from .fcm_service import send_push_notification

@api_view(["POST"])
@permission_classes([AllowAny])   # change to IsAuthenticated in production
def send_notification(request):
    token = request.data.get("token")
    title = request.data.get("title")
    body = request.data.get("body")
    data = request.data.get("data", {})

    if not token or not title or not body:
        return Response({"error": "Missing fields (token/title/body)"}, status=400)

    result = send_push_notification(token, title, body, data)
    return Response(result)

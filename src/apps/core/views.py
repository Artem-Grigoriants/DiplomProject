from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import rollbar

class RollbarTestView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Этот код вызовет AttributeError, который будет перехвачен Rollbar middleware
        a = None
        a.hello()
        return Response({"message": "This message should not appear."})


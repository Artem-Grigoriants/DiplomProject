from rest_framework import generics, permissions
from .models import User
from .serializers import CustomUserSerializer, CustomUserCreateSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating the authenticated user's details.
    Includes additional fields: company, position, and type.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserCreateView(generics.CreateAPIView):
    """
    View for user registration.
    Uses the CustomUserCreateSerializer to handle additional fields.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [permissions.AllowAny]
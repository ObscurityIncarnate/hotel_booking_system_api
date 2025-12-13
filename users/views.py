from .models import User
from .serializers.common import UserSerializer
from rest_framework import generics
from .serializers.tokens import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class SignUpView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     return super().create(request, *args, **kwargs)
    
    
# class SignUpView(APIView):
#   def post(self, request):
#     serializer = UserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response({ "message": 'Sign up successful' })

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
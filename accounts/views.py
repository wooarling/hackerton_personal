from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer

# -----------------------------
# HTML 렌더링
# -----------------------------
def register_page(request):
    return render(request, 'accounts/register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('board:post_list')  # 로그인 성공 → 루트 게시글 리스트
        else:
            return render(request, 'accounts/login.html', {'error': '아이디 또는 비밀번호가 잘못되었습니다.'})
    return render(request, 'accounts/login.html')


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('accounts:login_page')


# -----------------------------
# 회원가입 API
# -----------------------------
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if request.content_type != 'application/json':
            data = {
                'username': request.POST.get('username'),
                'password': request.POST.get('password'),
                'name': request.POST.get('name'),
                'nickname': request.POST.get('nickname'),
                'phone': request.POST.get('phone'),
                'gender': request.POST.get('gender'),
                'email': request.POST.get('email'),
                'birth_date': request.POST.get('birth_date'),
            }
        else:
            data = request.data

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if request.content_type != 'application/json':
                return redirect('accounts:login_page')
            return Response({"message": "회원가입 성공"}, status=201)
        return Response(serializer.errors, status=400)


# -----------------------------
# JWT 로그인 API
# -----------------------------
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]

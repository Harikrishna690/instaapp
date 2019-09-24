from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets
from .serializers import UserSerializer, LikedSerializer, CommentSerializer, ImageSerializer, GetUserSerializer
from .models import *
from .filters import *
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def loginpage(request):
    return render(request, 'll.html', {})


def getuser(request):
    print(request.user)


def userLogin(request):
    return HttpResponse('', status=200 if request.user.is_authenticated else 401)


@csrf_exempt
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            login(request, user)
            return redirect('/home')
    return render(request, '/home')


def logout_user(request):
    logout(request)
    return redirect('/loginpage')


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = UserFilter
    search_fields = ('username', 'id', )

    @action(detail=False, methods=['get'])
    def get(self, request):
        instance = request.user
        serializer = GetUserSerializer(instance)
        return Response(serializer.data)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Images.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, )
    filter_class = ImagesFilter
    ordering = ('uploaded_date', )

    @action(detail=False, methods=['get'])
    def get(self, request):
        offset = int(request.query_params.get('offset'))
        count = int(request.query_params.get('count'))

        return JsonResponse(['/index.png', '/logo192.png', '/logo512.png'], safe=False)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_class = CommentsFilter


class LikedViewSet(viewsets.ModelViewSet):
    serializer_class = LikedSerializer
    queryset = Liked.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_class = LikedFilter


from .serializer import  TopicSerializer, ResultsSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView,ListCreateAPIView
from rest_framework.views import APIView
from .models import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
def index(request):
    return HttpResponse('API')


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

class TopicList(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (IsAuthenticated,)


class ResultsPost(ListCreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    # permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ['user__username','topic__title','points']



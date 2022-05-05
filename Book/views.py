from .serializer import  TopicSerializer, ResultsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from django.http import HttpResponse
def index(request):
    return HttpResponse('API')



class TopicList(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class ResultsPost(CreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
from .serializer import QuestionSerializer, ChoiceSerializer, AnswerListSerializer, TopicSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from django.http import HttpResponse
def index(request):
    return HttpResponse('API')

class GetQuestion(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(visible=True).all()


class QuestionAnswer(APIView):
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAuthenticated,)
    def post(self,requests):
        answer = AnswerSerializer(data=requests.data)
        if answer.is_valid():
            answer.save()
        return Response(status= 201)

class Answers(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer

class Choices(ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class TopicList(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


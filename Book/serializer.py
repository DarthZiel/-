from rest_framework import serializers
from .models import Answer, Question, Choice, User, Topic, Theory


class ChoiceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Choice
        fields = ['pk', 'title', 'points', 'percent']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )

    class Meta:
        model = Question
        fields = ['pk', 'title', 'choices']


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    question = serializers.SlugRelatedField(slug_field='title',queryset= Question.objects.all())
    choice = serializers.SlugRelatedField(slug_field='title', queryset= Choice.objects.all())
    class Meta:
        model = Answer
        fields = ['user','question','choice']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AnswerListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    question = QuestionSerializer
    choice = ChoiceSerializer
    class Meta:
        model = Answer
        fields = "__all__"


# Список тем
class TopicSerializer(serializers.Serializer):
    class Meta:
        model = Topic
        fields = "__all__"

class TheorySerializer(serializers.Serializer):
    class Meta:
        model = Theory
        fields = "__all__"
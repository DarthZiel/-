from rest_framework import serializers
from .models import Question, Choice, User, Topic, Results


class ChoiceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Choice
        fields = ['pk', 'title', 'points']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )

    class Meta:
        model = Question
        fields = ['pk', 'title', 'choices']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




# Список тем
class TopicSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set', )
    class Meta:
        model = Topic
        fields = ['title','questions']


class ResultsSerializer(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(slug_field='title', queryset=Topic.objects.all())
    class Meta:
        model = Results
        fields = ['user', 'topic','points']
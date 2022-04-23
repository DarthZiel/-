from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fio = models.CharField(max_length=100, blank=True)
    class_title = models.CharField(max_length=30, blank=True)

class Topic(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема")
    def __str__(self):
        return self.title
class Theory(models.Model):
    title_id = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    content = models.TextField()
    def __str__(self):
        return self.title_id.title


class Question(models.Model):
    title = models.CharField(max_length=4096)
    practice_id = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    
    visible = models.BooleanField(default=False)

    def __str__(self):
           return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    points = models.FloatField()
    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title

        
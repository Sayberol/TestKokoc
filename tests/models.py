from django.db import models

from users.models import User


class Question(models.Model):
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Tests(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class TestQuestions(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.question

    class Meta:
        verbose_name = "Вопрос для теста"
        verbose_name_plural = "Вопросы для тестов"


class Answer(models.Model):
    text = models.TextField(max_length=1000)
    questions = models.ManyToManyField(Question, through='QuestionAnswer')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class QuestionRightAnswer(models.Model):
    right_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Правильный ответ на вопрос"
        verbose_name_plural = "Правильные ответы на вопросы"


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.question} {self.answer}"

    class Meta:
        verbose_name = "Вопрос - ответ"
        verbose_name_plural = "Вопросы - ответы"


class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return F"{self.user}: {self.points} points"

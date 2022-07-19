from django.contrib import admin

from tests.models import Answer, Question, QuestionAnswer, QuestionRightAnswer, TestQuestions, Tests

admin.site.register(Tests)
admin.site.register(TestQuestions)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(QuestionRightAnswer)


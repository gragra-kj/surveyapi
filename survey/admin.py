from django.contrib import admin

# Register your models here.
from .models import ResponseModel,QuestionModel,AnswerModel,Choice,SurveyModel

admin.site.register(SurveyModel)
admin.site.register(ResponseModel)
admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
admin.site.register(Choice)
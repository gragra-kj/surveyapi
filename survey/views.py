from django.shortcuts import render
from rest_framework import viewsets
from .models import SurveyModels,QuestionModels,ResponseModels,AnswerModels,Choice
from .serializers import SurveySerializer,QuestionSerializers,ResponseSerializer,AnswerSerializers,ChoiceSerializer
from rest_framework import permissions

# Create your views here
class SurveyViewSets(viewsets.ModelViewSet):
    queryset=SurveyModels.objects.all()
    serializer_class=SurveySerializer
    permission_classes=[]
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset=QuestionModels.objects.all()
    serializer_class=QuestionSerializers
    permission_classes=[]    
class ResponseViewSet(viewsets.ModelViewSet):
    queryset=ResponseModels.objects.all()
    serializer_class=ResponseSerializer
    permission_classes=[]
    
class AnswerViewset(viewsets.ModelViewSet):
    queryset=AnswerModels.objects.all()
    serializer_class=AnswerSerializers 
    permission_classes=[]   
    
class ChoicesViewSets(viewsets.ModelViewSet):
    queryset=Choice.objects.all()
    serializer_class=ChoiceSerializer
    permission_classes=[]    
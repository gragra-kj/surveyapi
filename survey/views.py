from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import SurveyModel,QuestionModel,ResponseModel,AnswerModel,Choice
from .serializers import SurveySerializer,QuestionSerializer,ResponseSerializer,AnswerSerializer,ChoiceSerializer
from rest_framework import permissions

# Create your views here
class SurveyViewSets(viewsets.ModelViewSet):
    queryset=SurveyModel.objects.all()
    serializer_class=SurveySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset=QuestionModel.objects.all()
    serializer_class=QuestionSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]  
      
class ResponseViewSet(viewsets.ModelViewSet):
    queryset=ResponseModel.objects.all()
    serializer_class=ResponseSerializer
    permission_classes=[permissions.AllowAny]
    
    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)
    
class AnswerViewset(viewsets.ModelViewSet):
    queryset=AnswerModel.objects.all()
    serializer_class=AnswerSerializer
    permission_classes=[permissions.AllowAny]   
    
    # def perform_create(self, serializer):
    #     user = self.request.user if self.request.user.is_authenticated else None
    #     serializer.save(user=user)
    
class ChoicesViewSets(viewsets.ModelViewSet):
    queryset=Choice.objects.all()
    serializer_class=ChoiceSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]    
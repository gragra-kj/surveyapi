from .models import SurveyModels,QuestionModels,ResponseModels,AnswerModels,Choice

from rest_framework import  serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model=SurveyModels
        fields=['id','title','description','created_at']
        
        
class QuestionSurvey(serializers.ModelSerializer):
    class Meta:
        model=QuestionModels
        fields=['id','survey','question_type']
        
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text']
             
class ResponseSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=ResponseModels
        fields=['id','user','survey','submitted_at']
        
    def create(self, validated_data):
        # Auto-assign user if present in context
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
        return super().create(validated_data)
    
        
class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model=AnswerModels
        fields=['id','response','answer_text','question','selected_choice']   
        
                  
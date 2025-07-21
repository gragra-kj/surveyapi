from .models import SurveyModel,QuestionModel,ResponseModel,AnswerModel,Choice

from rest_framework import  serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model=SurveyModel
        fields=['id','title','description','created_at']
        
class ChoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text']        
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')
    class Meta:
        model=QuestionModel
        fields=['id','survey','question_type','text','choices']
        

             
class ResponseSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=ResponseModel
        fields=['id','user','survey','submitted_at']
        
    def create(self, validated_data):
        # Auto-assign user if present in context
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
        return super().create(validated_data)
    
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = ['id', 'response', 'question', 'selected_choice', 'answer_text']

    def validate(self, data):
        question = data.get('question')
        selected_choice = data.get('selected_choice')

        if selected_choice and selected_choice.question != question:
            raise serializers.ValidationError("Selected choice does not belong to the given question.")

        return data    
        
                  
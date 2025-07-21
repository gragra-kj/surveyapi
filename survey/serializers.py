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
    
        
# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnswerModel
#         fields = ['id', 'response', 'question', 'selected_choice', 'answer_text']

#     def validate(self, data):
#         question = data.get('question')
#         selected_choice = data.get('selected_choice')

#         if selected_choice and selected_choice.question != question:
#             raise serializers.ValidationError("Selected choice does not belong to the given question.")

#         return data    


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = ['id', 'response', 'question', 'selected_choice', 'answer_text']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.question.question_type == 'text':
            rep.pop('selected_choice', None)
        else:
            rep.pop('answer_text', None)
        return rep

    def validate(self, data):
        question = data.get('question')
        selected_choice = data.get('selected_choice')
        answer_text = data.get('answer_text')

        if question.question_type == 'multiple_choice':
            if not selected_choice:
                raise serializers.ValidationError("Multiple choice question must have a selected choice.")
            if selected_choice.question != question:
                raise serializers.ValidationError("Selected choice does not belong to the given question.")
            data['answer_text'] = None  # optional, to avoid saving useless text

        elif question.question_type == 'text':
            if not answer_text:
                raise serializers.ValidationError("Text question must have an answer.")
            data['selected_choice'] = None  # optional, to avoid saving junk choice

        return data

        
                  
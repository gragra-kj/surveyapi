from django.db import models

# Create your models here.
from django.contrib.auth.models import User
QUESTION_TYPES = [
    ('text', 'Text'),
    ('choice', 'Multiple Choice'),
    ('rating', 'Rating'),
]


class SurveyModels(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return {self.title}
        
    
class QuestionModels(models.Model):
    survey=models.ForeignKey(SurveyModels,on_delete=models.CASCADE,related_name='questions')
    text=models.TextField(max_length=500)
    question_type=models.CharField(max_length=60,choices=QUESTION_TYPES,default=text)
    required=models.BooleanField(default=True)
    
    def __str__(self):
        return self.text
    
class ResponseModels(models.Model):
    survey=models.ForeignKey(SurveyModels,on_delete=models.CASCADE,related_name="responses")
    submitted_at=models.DateTimeField(auto_now_add=True)
    #respondent=models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        if self.user:
            return f"Response by {self.user.username} on {self.survey.title}"
        return f"Anonymous response to {self.survey.title}"
    
class AnswerModels(models.Model):
    response=models.ForeignKey(ResponseModels,on_delete=models.CASCADE,related_name="answers")
    question=models.ForeignKey(QuestionModels,on_delete=models.CASCADE, related_name="answers")
    answer_text=models.TextField()
    #surveyor=models.ForeignKey(User,on_delete=models.CASCADE)   
    def __str__(self):
        return f"Answer to: {self.question.text}"        
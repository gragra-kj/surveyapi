from django.db import models

# Create your models here.
from django.contrib.auth.models import User
QUESTION_TYPES = [
    ('text', 'Text'),
    ('choice', 'Multiple Choice'),
    ('rating', 'Rating'),
]


class SurveyModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
        
    
# class QuestionModel(models.Model):
#     TEXT = 'text'
#     MULTIPLE_CHOICE = 'mcq'

#     QUESTION_TYPES = [
#         (TEXT, 'Text'),
#         (MULTIPLE_CHOICE, 'Multiple Choice'),
#     ]

#     survey = models.ForeignKey(SurveyModel, on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default=TEXT)

#     def __str__(self):
#         return self.text

class QuestionModel(models.Model):
    TEXT = 'text'
    MULTIPLE_CHOICE = 'multiple_choice'

    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]

    survey = models.ForeignKey(SurveyModel, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    text = models.TextField()
    
    def __str__(self):
        return self.text
class ResponseModel(models.Model):
    survey=models.ForeignKey(SurveyModel,on_delete=models.CASCADE,related_name="responses")
    submitted_at=models.DateTimeField(auto_now_add=True)
    #respondent=models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        if self.user:
            return f"Response by {self.user.username} on {self.survey.title}"
        return f"Anonymous response to {self.survey.title}"
class Choice(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.text} (Q: {self.question.text[:30]}...)"        
    
class AnswerModel(models.Model):
    response = models.ForeignKey(ResponseModel, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    answer_text = models.TextField(blank=True, null=True)
    # response=models.ForeignKey(ResponseModel,on_delete=models.CASCADE,related_name="answers")
    # question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE, related_name="answers")
    # selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    # answer_text=models.TextField()
    #surveyor=models.ForeignKey(User,on_delete=models.CASCADE)   
    def __str__(self):
        if self.choice:
            return f"{self.question.text} -> {self.choice.text}"
        elif self.answer_text:
            return f"{self.question.text} -> {self.answer_text}"
        return f"{self.question.text} -> No Answer"     



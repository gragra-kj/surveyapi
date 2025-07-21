from rest_framework.routers import DefaultRouter

from .views import SurveyViewSets,QuestionViewSet,ResponseViewSet,AnswerViewset,ChoicesViewSets
from django.urls import include,path

router=DefaultRouter()

router.register('surveys',SurveyViewSets)
router.register('questions',QuestionViewSet)
router.register('responses',ResponseViewSet)
router.register('answers',AnswerViewset)
router.register('choices',ChoicesViewSets)

urlpatterns=[
    path('',include(router.urls))
]
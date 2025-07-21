# 📝 Django Survey API

This is a Django REST Framework project that allows users to create surveys, add questions, collect responses, and analyze answers. It supports both text and multiple-choice questions.

## 🚀 Features

- User registration and authentication
- Create and manage surveys
- Add questions to surveys (text or multiple-choice)
- Add choices to multiple-choice questions
- Submit responses to surveys
- Save text answers or selected choices
- API-based architecture using Django REST Framework
- Admin panel for managing data

## 🧱 Models

- **SurveyModel**: Stores survey title, description, and creation time.
- **QuestionModel**: Linked to a survey, contains question text and type (`text` or `multiple_choice`).
- **Choice**: Linked to a question (for multiple-choice), stores option text.
- **ResponseModel**: Represents a user's submission to a survey.
- **AnswerModel**: Stores individual answers in a response (text or selected choice).

## 📦 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/surveys/` | GET, POST | List or create surveys |
| `/api/questions/` | GET, POST | List or create questions |
| `/api/choices/` | GET, POST | List or create choices |
| `/api/responses/` | GET, POST | Submit or list responses |
| `/api/answers/` | GET, POST | List or submit answers |

> All endpoints are protected by authentication except reading surveys and questions.

## 🔐 Authentication

Uses Django's default user model. Token authentication or session-based login can be enabled.

## 🛠️ Setup Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/survey-api.git
   cd survey-api
2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate
3. Install dependencies:
     ```bash
     pip install -r requirements.txt
4. Apply migrations:
   ```bash
   python manage.py migrate

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
6. Run server:
   ```bash
   python manage.py runserver

## Seeding Example Data
```bash
from surveys.models import SurveyModel, QuestionModel, Choice

survey = SurveyModel.objects.create(title="Customer Satisfaction Survey", description="We value your feedback!")

q1 = QuestionModel.objects.create(survey=survey, question_text="How satisfied are you with our service?", question_type="multiple_choice")
Choice.objects.create(question=q1, text="Very satisfied")
Choice.objects.create(question=q1, text="Satisfied")
Choice.objects.create(question=q1, text="Neutral")
Choice.objects.create(question=q1, text="Dissatisfied")

q2 = QuestionModel.objects.create(survey=survey, question_text="Any suggestions?", question_type="text")





    

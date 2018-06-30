from django.urls import path

from flashcard import views


urlpatterns = [
    path('add/', views.CreateFlashCard.as_view()),
]

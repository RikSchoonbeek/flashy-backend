from django.urls import path

from flashcard import views


urlpatterns = [
    path('add/', views.CreateFlashCard.as_view()),
    path('get_languages/', views.GetLanguageList.as_view()),
]

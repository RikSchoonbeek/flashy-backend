from django.contrib import admin

from flashcard import models


@admin.register(models.FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    list_display = ('problem', 'topic', 'language')


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', )


@admin.register(models.Selection)
class SelectionAdmin(admin.ModelAdmin):
    list_display = ('flashcard', 'index_from', 'index_to')

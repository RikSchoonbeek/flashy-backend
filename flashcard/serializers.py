from rest_framework import serializers

from flashcard.models import FlashCard, ProgrammingLanguage, Topic, Selection


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('code', 'problem', 'topic', 'language', 'source')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('name', )


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ('name', )


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ('index_from', 'index_to', 'flashcard', )

from rest_framework import serializers

from flashcard.models import FlashCard, Topic, Language, Source


class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('code', 'problem', 'topic', 'language', 'source')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('name', )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('name', 'version', )


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('index_from', 'index_to', 'flashcard', )

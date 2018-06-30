from rest_framework.views import APIView

from flashcard.serializers import FlashCardSerializer, TopicSerializer, LanguageSerializer, \
    SelectionSerializer
from rest_framework.views import

from flashcard.utils import separate_flashcard_data, save_topic, \
    return_selection_data_dict, save_selection


class CreateFlashCard(APIView):
    """
    This view saves an instance of a flashcard to the database.

    Incoming data format:
    {
        'code': code,
        'problem': problem,
        'topic': topic,
        'language': language,
        'source': source,
        'selections': (
                (1, 30),
                (45,56),
            )
    }
    """
    def post(self, request, format=None):
        topic_data, flashcard_data, selection_list = separate_flashcard_data(request.data)

        # save topic and return foreign key instance
        topic = save_topic(topic_data)

        # update foreign key instance in flashcard_data
        flashcard_data['topic'] = topic

        # save flashcard and return flashcard instance
        flashcard_serializer = FlashCardSerializer(flashcard_data)
        flashcard = flashcard_serializer.save()

        # save flashcard selections, use returned foreign key instance
        for selection in selection_list:
            index_from = int(selection[0])
            index_to = int(selection[1])
            selection_data = return_selection_data_dict(
                index_from,
                index_to,
                flashcard
            )
            save_selection(selection_data)

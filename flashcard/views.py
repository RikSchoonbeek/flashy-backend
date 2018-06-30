from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView

from flashcard.serializers import FlashCardSerializer, ProgrammingLanguageSerializer, \
    TopicSerializer, SelectionSerializer

from flashcard.utils import separate_flashcard_data, save_topic, \
    return_selection_data_dict, save_selection, add_prog_lang_to_flashcard_data

from flashcard.models import ProgrammingLanguage


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
    @csrf_exempt
    def post(self, request, format=None):
        print("request.data")
        print(request.data)
        topic_data, flashcard_data, selection_list = separate_flashcard_data(request.data)

        # save topic and return foreign key instance
        topic = save_topic(topic_data)

        # # update foreign key instance in flashcard_data
        # flashcard_data['topic'] = topic

        # add prog lang instance to flashcard_data
        flashcard_data = add_prog_lang_to_flashcard_data(flashcard_data)
        # save flashcard and return flashcard instance
        flashcard_serializer = FlashCardSerializer(data=flashcard_data)
        if flashcard_serializer.is_valid():
            flashcard = flashcard_serializer.save()
        else:
            print(f"flashcard_serializer.errors: {flashcard_serializer.errors}")

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


class GetLanguageList(APIView):
    """
    Returns a list of all possible languages.
    """
    @csrf_exempt
    def get(self, request):
        languages = ProgrammingLanguage.objects.all()
        serializer = ProgrammingLanguageSerializer(languages, many=True)
        return Response(serializer.data)

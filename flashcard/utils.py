from flashcard.models import ProgrammingLanguage, Topic
from flashcard.serializers import TopicSerializer, SelectionSerializer

def separate_flashcard_data(all_data):
    """
    Takes a dict with all data send from frontend to backend, returns separated data
    for flashcard, selection_list and topic.
    """
    flashcard_data = {}
    selection_list = None
    topic_data = {}
    for key, value in all_data.items():
        if key == 'selections':
            selection_list = value
        elif key == 'topic':
            topic_data['name'] = value
        else:
            flashcard_data[key] = value
    return topic_data, flashcard_data, selection_list


def add_prog_lang_to_flashcard_data(flashcard_data):
    """
    Takes the flashcard_data dict, substitutes the
    """
    programming_language = ProgrammingLanguage.objects.get(name=flashcard_data['language'])
    flashcard_data['language'] = programming_language
    return flashcard_data


def save_topic(topic_data):
    """
    Saves the topic to database, if it doesn't exist already.
    """
    try:
        topic = Topic.objects.get(name=topic_data['name'])
    except Topic.DoesNotExist:
        topic_serializer = TopicSerializer(data=topic_data)
        if topic_serializer.is_valid():
            topic = topic_serializer.save()
        else:
            print(f"topic_serializer.errors: {topic_serializer.errors}")
    return topic


def return_selection_data_dict(index_from, index_to, flashcard_object):
    """
    Returns an dict containing selection data, to be fed to the SelectionSerializer.

    Takes:
    - index_from and index_to as integers
    - flashcard_object as flashcard model instance

    returns dict with format:
    {
        'index_from': index_from,
        'index_to': index_to,
        'flashcard': flashcard_object,
    }
    """
    return {
        'index_from': index_from,
        'index_to': index_to,
        'flashcard': flashcard_object,
    }


def save_selection(selection_data):
    """
    Takes a dict of selection data, saves instance to DB.
    """
    selection_serializer = SelectionSerializer(data=selection_data)
    if selection_serializer.is_valid():
        return selection_serializer.save()
    else:
        print(f"selection_serializer.errors: {selection_serializer.errors}")

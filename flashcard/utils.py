from flashcard.models import Topic
from flashcard.serialiserz import TopicSerializer, SelectionSerializer

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


def save_topic(topic_data):
    """
    Saves the topic to database, if it doesn't exist already.
    """
    # Check if topic already in DB
    try:
        topic = Topic.objects.get(name=topic_data)
    except Topic.DoesNotExist:
        topic_serializer = TopicSerializer(topic_data)
        topic = topic_serializer.save()
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
    selection_serializer = SelectionSerializer(selection_data)
    return selection_serializer.save()

import csv
from django.core.management.base import BaseCommand

from flashcard.models import ProgrammingLanguage


class Command(BaseCommand):
    help = "Adds programming languages to the DB from languages.csv"

    def handle(self, *args, **options):
        with open('languages.csv', mode='r') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',')
            for row in filereader:
                self.handle_row(row)

    def handle_row(self, row):
        """
        Calls function to check if language of current row is already in db, and function
        to save it to DB if it isn't found in DB already.
        """
        language_name = row[0]
        # Check if programming language with this name is already in DB
        language = self.check_if_language_exists_in_db(language_name)
        # If not, save it
        if not language:
            self.save_language(language_name)



    def check_if_language_exists_in_db(self, language_name):
        """
        Checks if language is in DB or not, returns language object if found, else returns None.
        Takes language name as string.
        """
        language = None
        try:
            language = ProgrammingLanguage.objects.get(name=language_name)
        except ProgrammingLanguage.DoesNotExist:
            pass
        return language

    def save_language(self, language_name):
        """
        Saves language to DB, takes language name as string.
        """
        language = ProgrammingLanguage(name=language_name)
        language.save()



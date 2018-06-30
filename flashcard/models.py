from django.db import models


class FlashCard(models.Model):
    code = models.TextField()
    problem = models.CharField(max_length=511)
    topic = models.ForeignKey('Topic',
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              )
    language = models.ForeignKey('ProgrammingLanguage',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 )
    source = models.CharField(max_length=511,
                              blank=True,
                              null=True,
                              )

    def __str__(self):
        return self.problem


class Topic(models.Model): #(relates to a user in a many to many relationship)
    name = models.CharField(max_length=255)
    # user = models.ForeignKey() # many to many

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=127)
    version = models.CharField(max_length=127,
                               blank=True,
                               null=True,
                               )

    def __str__(self):
        name = self.name
        if self.version:
            name += (' ' + self.version)
        return name


class Selection(models.Model): #(related to a specific card) - each selection on  a card get's it's own entry - index from + index to
    index_from = models.PositiveIntegerField()
    index_to = models.PositiveIntegerField()
    flashcard = models.ForeignKey(FlashCard, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flashcard.problem}: {self.index_from} - {self.index_to}"

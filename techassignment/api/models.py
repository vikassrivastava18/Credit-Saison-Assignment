from django.db import models


class Searched(models.Model):
    card_number = models.CharField(unique=False, max_length=20, null=False, blank=False)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Card {0}, was searched at: {1}".format(self.card_number, self.time_stamp)
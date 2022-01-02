from django.db import models


class Searched(models.Model):
    card_number = models.CharField(unique=True, max_length=20)
    hits = models.IntegerField(default=1)
    first_time_stamp = models.DateTimeField(auto_now=True)
    latest_time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Card {0}, has been searched {1} times".format(self.card_number, self.hits)
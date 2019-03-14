from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from evaluation.models import Evaluating


class touristSpot(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    approved = models.BooleanField()

    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    evaluations = models.ManyToManyField(Evaluating)

    def __str__(self):
        return self.name

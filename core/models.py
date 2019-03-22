from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from evaluation.models import Evaluating
from adresses.models import Address


class DocumentIdentification(models.Model):
    description = models.CharField(max_length=150)


class TouristSpot(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    approved = models.BooleanField()

    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    evaluations = models.ManyToManyField(Evaluating)
    adresses = models.ForeignKey(Address, on_delete=models.CASCADE)
    document_Itentification = models.OneToOneField(DocumentIdentification, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='touristic_point', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_description_complete(self):
        return "%s - %s" %(self.name, self.description)

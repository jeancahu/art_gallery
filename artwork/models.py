from django.db import models
from collection.models import Collection

class Artwork(models.Model):
    name = models.CharField(max_length=256)
    img_url = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    collection_choices = ((x.name, x.name) for x in Collection.objects.all())
    collection = models.CharField(blank=True, choices=collection_choices, max_length=24) # TODO chg by collection object list
    # author = models.IntegerField() # TODO chg by collection object list

    def __str__(self):
        return self.name

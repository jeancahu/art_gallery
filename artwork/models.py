from django.db import models

class Artwork(model.Model):
    name = models.CharField(max_length=256)
    img_url = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    collection = models.IntField(max_length=256) # TODO chg by collection object list

    def __str__(self):
        return self.name

from django.db import models

class Artwork(models.Model):
    name = models.CharField(max_length=256)
    img_url = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    collection = models.IntegerField() # TODO chg by collection object list
    # author = models.IntegerField() # TODO chg by collection object list

    def __str__(self):
        return self.name

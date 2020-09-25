from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=256)
    # category = models.CharField(max_length=256) # TODO subtitle gray
    banner_url = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    # created = models.DateTimeField(auto_now_add=True)
    # collection = models.IntegerField() # TODO chg by collection object list

    def __str__(self):
        return self.name

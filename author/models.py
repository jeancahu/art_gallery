from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    biography = models.CharField(max_length=256)

    def __str__(self):
        return self.name

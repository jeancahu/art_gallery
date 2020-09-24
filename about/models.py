from django.db import models

class About(models.Model):
    description = models.CharField(max_length=256)
    banner_url = models.CharField(max_length=256)

    def __str__():
        return "About"

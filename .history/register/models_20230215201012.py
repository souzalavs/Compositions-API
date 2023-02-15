from django.db import models

class Composition(models.Model):
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    composer = models.CharField(max_length=100)

    def __str__(self):
        return self.title
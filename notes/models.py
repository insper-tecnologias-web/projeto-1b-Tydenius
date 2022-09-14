from operator import truediv
from django.db import models

    
class Tag(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        string = f"{self.name}"
        return string

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Note(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, default=0, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        string = f"{self.id}. {self.title}"
        return string
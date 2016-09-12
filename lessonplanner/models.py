from django.db import models
from django.utils import timezone

# Create your models here.


class Lesson(models.Model):
    author = models.ForeignKey('auth.User')
    className = models.CharField(max_length=35)
    date = models.DateTimeField(
            blank=True, null=True)
    unit = models.CharField(max_length=35)
    chapter = models.CharField(max_length=35)
    summary = models.TextField()
    materials = models.TextField()
    description = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.unit

from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model): #models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    view_count = models.PositiveIntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
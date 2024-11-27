from django.db import models


# Create your models here.
class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tags")

    class Meta:
        ordering = ["complete", "-datetime"]


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

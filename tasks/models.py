from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=300)
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE)

    """def __str__(self):
        return self.name"""
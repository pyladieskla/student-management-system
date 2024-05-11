from django.db import models


class Pupil(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50, null=False, blank=False)
    level = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} is of age {self.age}"

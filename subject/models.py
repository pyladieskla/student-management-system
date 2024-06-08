from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    code = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name + " - " + self.code
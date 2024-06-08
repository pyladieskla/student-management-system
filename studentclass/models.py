from django.db import models

class StudentClass(models.Model):
    name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, related_name='classes', null=True, blank=True)

    def __str__(self):
        return self.name
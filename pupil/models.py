from django.db import models


class Pupil(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50, null=False, blank=False)
    student_class = models.ForeignKey('studentclass.StudentClass', on_delete=models.PROTECT, related_name='pupils', null=True, blank=True)
    gender = models.CharField(max_length=6, null=False, blank=False)
    is_eligible_for_prefect = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} is of age {self.age}"

    def save(self, *args, **kwargs):
        if self.age >= 10:
            self.is_eligible_for_prefect = True
        super(Pupil, self).save(*args, **kwargs)
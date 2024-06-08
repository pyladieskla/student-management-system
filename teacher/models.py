from django.db import models

MALE = 'male'
FEMALE = 'female'
gender_choices = [
        (MALE, MALE),
        (FEMALE, FEMALE),
    ]
class Teacher(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=gender_choices, blank=False, null=False)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    subjects = models.ManyToManyField('subject.Subject', related_name='teachers')
    

    def __str__(self):
        return self.name + " - " + self.gender
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper() + " try"
        super(Teacher, self).save(*args, **kwargs)
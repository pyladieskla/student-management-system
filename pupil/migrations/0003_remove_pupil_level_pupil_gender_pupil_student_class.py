# Generated by Django 5.0.6 on 2024-05-11 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupil', '0002_alter_pupil_name'),
        ('studentclass', '0003_alter_studentclass_class_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupil',
            name='level',
        ),
        migrations.AddField(
            model_name='pupil',
            name='gender',
            field=models.CharField(default='male', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pupil',
            name='student_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pupils', to='studentclass.studentclass'),
        ),
    ]

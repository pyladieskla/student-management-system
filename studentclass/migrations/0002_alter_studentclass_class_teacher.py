# Generated by Django 5.0.6 on 2024-05-11 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentclass', '0001_initial'),
        ('teacher', '0003_teacher_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclass',
            name='class_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='teacher.teacher'),
        ),
    ]
# Generated by Django 4.2.11 on 2024-09-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examinationapp', '0007_examinationuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]

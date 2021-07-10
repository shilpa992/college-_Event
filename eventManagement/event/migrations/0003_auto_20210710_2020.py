# Generated by Django 3.2.4 on 2021-07-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='college_event',
            name='college',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='college_event',
            name='college_type',
            field=models.CharField(choices=[('UG', 'UG'), ('PG', 'PG'), ('Engineering', 'Engineering'), ('diploma', 'diploma')], max_length=200, null=True),
        ),
    ]

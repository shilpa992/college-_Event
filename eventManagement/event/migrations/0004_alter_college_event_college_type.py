# Generated by Django 3.2.4 on 2021-07-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20210710_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college_event',
            name='college_type',
            field=models.CharField(choices=[('UG', 'UG'), ('PG', 'PG'), ('Engineering', 'Engineering'), ('diploma', 'diploma')], max_length=200),
        ),
    ]

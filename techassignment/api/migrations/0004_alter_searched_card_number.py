# Generated by Django 4.0 on 2022-01-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_first_time_stamp_searched_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searched',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
    ]
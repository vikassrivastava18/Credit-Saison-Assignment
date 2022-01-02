# Generated by Django 4.0 on 2022-01-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Searched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20, unique=True)),
                ('hits', models.IntegerField(default=1)),
                ('first_time_stamp', models.DateTimeField(auto_now=True)),
                ('latest_time_stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
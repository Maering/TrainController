# Generated by Django 2.1.7 on 2019-04-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrainControllerApp', '0005_merge_20190403_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='user',
        ),
    ]
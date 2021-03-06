# Generated by Django 2.1.7 on 2019-03-30 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baudrate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SerialPort',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parity', models.PositiveSmallIntegerField()),
                ('baudrate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrainControllerApp.Baudrate')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('lokid', models.PositiveSmallIntegerField(unique=True)),
            ],
        ),
    ]

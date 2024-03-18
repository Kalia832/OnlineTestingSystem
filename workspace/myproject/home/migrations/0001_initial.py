# Generated by Django 4.2 on 2023-06-22 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('qid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.TextField()),
                ('a', models.CharField(max_length=255)),
                ('b', models.CharField(max_length=255)),
                ('c', models.CharField(max_length=255)),
                ('d', models.CharField(max_length=255)),
                ('ans', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('testattempted', models.IntegerField()),
                ('points', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('resultid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('attends', models.IntegerField()),
                ('right', models.IntegerField()),
                ('wront', models.IntegerField()),
                ('points', models.FloatField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
    ]
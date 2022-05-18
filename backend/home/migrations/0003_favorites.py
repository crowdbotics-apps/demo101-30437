# Generated by Django 2.2.24 on 2022-05-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_favoritecars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('websiteName', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('timesVisited', models.BigIntegerField()),
            ],
        ),
    ]
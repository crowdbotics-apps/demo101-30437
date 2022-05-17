# Generated by Django 2.2.24 on 2022-05-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=256)),
                ('model', models.CharField(max_length=256)),
                ('year', models.BigIntegerField()),
            ],
        ),
    ]

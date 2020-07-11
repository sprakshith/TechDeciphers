# Generated by Django 3.0.6 on 2020-07-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaks',
            fields=[
                ('leakId', models.AutoField(primary_key=True, serialize=False)),
                ('leakImage', models.ImageField(upload_to='TechDeciphers_Leaks')),
                ('typeOfLeak', models.CharField(max_length=100)),
                ('heading', models.CharField(max_length=200)),
                ('miniHeading', models.CharField(max_length=200)),
                ('completeContent', models.TextField()),
                ('postAuthor', models.CharField(max_length=40)),
                ('postPublishDate', models.DateField()),
            ],
        ),
    ]

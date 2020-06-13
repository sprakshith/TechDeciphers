# Generated by Django 3.0.6 on 2020-06-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gadgets',
            fields=[
                ('gadgetId', models.AutoField(primary_key=True, serialize=False)),
                ('gadgetImage', models.ImageField(upload_to='')),
                ('typeOfGadget', models.CharField(max_length=100)),
                ('heading', models.CharField(max_length=200)),
                ('miniHeading', models.CharField(max_length=200)),
                ('miniContent', models.CharField(max_length=300)),
                ('completeContent', models.TextField()),
                ('postAuthor', models.CharField(max_length=40)),
                ('postPublishDate', models.DateField()),
            ],
        ),
    ]

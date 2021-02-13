# Generated by Django 3.0.6 on 2021-01-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('notebook_id', models.AutoField(primary_key=True, serialize=False)),
                ('notebook_image', models.ImageField(blank=True, null=True, upload_to='TechDeciphers_News')),
                ('heading', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('postAuthor', models.CharField(max_length=40)),
                ('postPublishDate', models.DateField()),
                ('isPublished', models.BooleanField(default=False)),
            ],
        ),
    ]
# Generated by Django 3.0.6 on 2020-07-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechDeciphers_Gadgets', '0007_auto_20200718_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadgets',
            name='heading',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gadgets',
            name='miniContent',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name='gadgets',
            name='miniHeading',
            field=models.CharField(max_length=180),
        ),
    ]
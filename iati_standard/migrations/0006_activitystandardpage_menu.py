# Generated by Django 2.2.9 on 2020-03-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_standard', '0005_auto_20200319_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitystandardpage',
            name='menu',
            field=models.TextField(blank=True, help_text='HTML data for the page menu', null=True),
        ),
    ]

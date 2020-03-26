# Generated by Django 2.2.9 on 2020-03-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0004_auto_20200302_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='active',
            field=models.BooleanField(blank=True, default=True, help_text='Only active members will be displayed on the site'),
        ),
    ]

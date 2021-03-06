# Generated by Django 2.0.8 on 2019-04-11 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('using_data', '0003_auto_20180828_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolsindexpage',
            name='social_media_image',
            field=models.ForeignKey(blank=True, help_text='This image will be used as the image for social media sharing cards.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]

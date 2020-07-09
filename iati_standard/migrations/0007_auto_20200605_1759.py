# Generated by Django 2.2.12 on 2020-06-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_standard', '0006_referencemenu_menu_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitystandardpage',
            name='ssot_root_slug',
            field=models.CharField(blank=True, help_text='Slug of the highest parent folder.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='standardguidancepage',
            name='ssot_root_slug',
            field=models.CharField(blank=True, help_text='Slug of the highest parent folder.', max_length=255, null=True),
        ),
    ]

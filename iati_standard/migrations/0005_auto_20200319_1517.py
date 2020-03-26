# Generated by Django 2.2.9 on 2020-03-19 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('iati_standard', '0004_referencemenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='iatistandardpage',
            name='latest_version_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='iati_standard.ActivityStandardPage'),
        ),
        migrations.AddField(
            model_name='iatistandardpage',
            name='reference_support_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
# Generated by Django 2.2.9 on 2020-02-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200217_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='use_legacy_template',
            field=models.BooleanField(blank=True, default=True, help_text='Use the legacy template with hard-coded text for front end display?'),
        ),
    ]

# Generated by Django 2.2.9 on 2020-04-14 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200303_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='use_legacy_template',
        ),
    ]

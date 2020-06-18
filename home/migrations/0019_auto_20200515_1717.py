# Generated by Django 2.2.12 on 2020-05-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_homepage_use_legacy_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='iati_in_action_description',
            field=models.TextField(blank=True, help_text='Optional: description for the IATI in action section', max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='iati_in_action_description_en',
            field=models.TextField(blank=True, help_text='Optional: description for the IATI in action section', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='iati_in_action_description_es',
            field=models.TextField(blank=True, help_text='Optional: description for the IATI in action section', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='iati_in_action_description_fr',
            field=models.TextField(blank=True, help_text='Optional: description for the IATI in action section', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='iati_in_action_description_pt',
            field=models.TextField(blank=True, help_text='Optional: description for the IATI in action section', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionfeatureditems',
            name='description',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500),
        ),
        migrations.AlterField(
            model_name='iatiinactionfeatureditems',
            name='description_en',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionfeatureditems',
            name='description_es',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionfeatureditems',
            name='description_fr',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionfeatureditems',
            name='description_pt',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionitems',
            name='description',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500),
        ),
        migrations.AlterField(
            model_name='iatiinactionitems',
            name='description_en',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionitems',
            name='description_es',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionitems',
            name='description_fr',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='iatiinactionitems',
            name='description_pt',
            field=models.CharField(blank=True, help_text='Optional: description for the item. Defaults to the selected page excerpt if left blank', max_length=500, null=True),
        ),
    ]

# Generated by Django 2.2.13 on 2021-02-01 14:34

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_spamsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='flexible_features',
            field=wagtail.core.fields.StreamField([('feature', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', help_text='Feature title.', icon='title')), ('description', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Button text.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Button URL.', required=False))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='flexible_features_en',
            field=wagtail.core.fields.StreamField([('feature', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', help_text='Feature title.', icon='title')), ('description', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Button text.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Button URL.', required=False))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='flexible_features_es',
            field=wagtail.core.fields.StreamField([('feature', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', help_text='Feature title.', icon='title')), ('description', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Button text.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Button URL.', required=False))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='flexible_features_fr',
            field=wagtail.core.fields.StreamField([('feature', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', help_text='Feature title.', icon='title')), ('description', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Button text.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Button URL.', required=False))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='flexible_features_pt',
            field=wagtail.core.fields.StreamField([('feature', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='title', help_text='Feature title.', icon='title')), ('description', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Button text.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='Button URL.', required=False))]))], blank=True, null=True),
        ),
    ]

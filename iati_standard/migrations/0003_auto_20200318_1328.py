# Generated by Django 2.2.9 on 2020-03-18 13:28

from django.db import migrations, models
import django.db.models.deletion
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
        ('iati_standard', '0002_social_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='iatistandardpage',
            name='live_tag',
            field=models.CharField(blank=True, help_text='Associated git release tag', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iatistandardpage',
            name='repo',
            field=models.URLField(blank=True, help_text='Git repo URL', null=True),
        ),
        migrations.CreateModel(
            name='ReferenceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssot_path', models.TextField(blank=True, help_text='Folder path of SSOT object', null=True)),
                ('tag', models.CharField(help_text='Associated git release tag', max_length=255)),
                ('language', models.CharField(default='en', help_text='Language', max_length=255)),
                ('ssot_root_slug', models.CharField(help_text='Slug of the highest parent folder.', max_length=255)),
                ('parent_path', models.TextField(blank=True, help_text='Parent path of object', null=True)),
                ('data', models.TextField(blank=True, help_text='HTML data for the page', null=True)),
            ],
            options={
                'verbose_name_plural': 'Reference data',
                'ordering': ['ssot_path'],
                'unique_together': {('ssot_path', 'tag')},
            },
        ),
        migrations.CreateModel(
            name='ActivityStandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('heading_en', models.CharField(blank=True, max_length=255, null=True)),
                ('heading_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('heading_es', models.CharField(blank=True, max_length=255, null=True)),
                ('heading_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('excerpt_en', models.TextField(blank=True, null=True)),
                ('excerpt_fr', models.TextField(blank=True, null=True)),
                ('excerpt_es', models.TextField(blank=True, null=True)),
                ('excerpt_pt', models.TextField(blank=True, null=True)),
                ('content_editor', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))], icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title'))])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock([('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))], icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))], blank=True, null=True)),
                ('content_editor_en', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))], icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title'))])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock([('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))], icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))], blank=True, null=True)),
                ('content_editor_fr', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))], icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title'))])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock([('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))], icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))], blank=True, null=True)),
                ('content_editor_es', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))], icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title'))])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock([('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))], icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))], blank=True, null=True)),
                ('content_editor_pt', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))], icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock('quote title'))])), ('aligned_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())], icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock([('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))], icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))], blank=True, null=True)),
                ('ssot_path', models.TextField(blank=True, help_text='Folder path of SSOT object', null=True)),
                ('tag', models.CharField(help_text='Associated git release tag', max_length=255)),
                ('data', models.TextField(blank=True, help_text='HTML data for the page', null=True)),
                ('data_en', models.TextField(blank=True, help_text='HTML data for the page', null=True)),
                ('data_fr', models.TextField(blank=True, help_text='HTML data for the page', null=True)),
                ('data_es', models.TextField(blank=True, help_text='HTML data for the page', null=True)),
                ('data_pt', models.TextField(blank=True, help_text='HTML data for the page', null=True)),
                ('has_been_recursed', models.BooleanField(default=False)),
                ('header_image', models.ForeignKey(blank=True, help_text='This is the image that will appear in the header banner at the top of the page. If no image is added a placeholder image will be used.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('social_media_image', models.ForeignKey(blank=True, help_text='This image will be used as the image for social media sharing cards.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
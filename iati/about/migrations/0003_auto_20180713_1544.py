# Generated by Django 2.0.5 on 2018-07-13 15:44

from django.db import migrations
import home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20180626_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='content_editor',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='content_editor_en',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='content_editor_es',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='content_editor_fr',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='content_editor_pt',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsubpage',
            name='content_editor',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsubpage',
            name='content_editor_en',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsubpage',
            name='content_editor_es',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsubpage',
            name='content_editor_fr',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutsubpage',
            name='content_editor_pt',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casestudypage',
            name='content_editor',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casestudypage',
            name='content_editor_en',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casestudypage',
            name='content_editor_es',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casestudypage',
            name='content_editor_fr',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casestudypage',
            name='content_editor_pt',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historypage',
            name='content_editor',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historypage',
            name='content_editor_en',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historypage',
            name='content_editor_es',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historypage',
            name='content_editor_fr',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historypage',
            name='content_editor_pt',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='content_editor',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='content_editor_en',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='content_editor_es',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='content_editor_fr',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='content_editor_pt',
            field=wagtail.core.fields.StreamField((('heading_2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('heading_4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image_figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', home.models.ImageAlignmentChoiceBlock()), ('caption', wagtail.core.blocks.RichTextBlock(required=False))), icon='image', label='Image figure')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('aligned_html', wagtail.core.blocks.StructBlock((('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', home.models.HTMLAlignmentChoiceBlock())), icon='code', label='Raw HTML')), ('document_box', wagtail.core.blocks.StreamBlock((('document_box_heading', wagtail.core.blocks.CharBlock(classname='title', help_text='Only one heading per box.', icon='title', required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', required=False))), icon='doc-full-inverse')), ('anchor_point', wagtail.core.blocks.CharBlock(help_text='Custom anchor points are expected to precede other content.', icon='order-down'))), blank=True, null=True),
        ),
    ]

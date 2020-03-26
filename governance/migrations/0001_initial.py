# Generated by Django 2.2.9 on 2020-02-27 09:22

from django.db import migrations, models
import django.db.models.deletion
import home.models
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembersAssemblyPage',
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
                ('members_title', models.CharField(help_text='Title for the members section', max_length=255)),
                ('members_title_en', models.CharField(help_text='Title for the members section', max_length=255, null=True)),
                ('members_title_fr', models.CharField(help_text='Title for the members section', max_length=255, null=True)),
                ('members_title_es', models.CharField(help_text='Title for the members section', max_length=255, null=True)),
                ('members_title_pt', models.CharField(help_text='Title for the members section', max_length=255, null=True)),
                ('social_media_image', models.ForeignKey(blank=True, help_text='This image will be used as the image for social media sharing cards.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ViceChairItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(help_text='Name of the chair', max_length=255)),
                ('name_en', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('name_fr', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('name_es', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('name_pt', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('bio', models.CharField(help_text='Short bio for the chair', max_length=255)),
                ('bio_en', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('bio_fr', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('bio_es', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('bio_pt', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('image', models.ForeignKey(blank=True, help_text='Optional: image for the chair', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('item', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='vice_chair_items', to='governance.MembersAssemblyPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChairItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(help_text='Name of the chair', max_length=255)),
                ('name_en', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('name_fr', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('name_es', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('name_pt', models.CharField(help_text='Name of the chair', max_length=255, null=True)),
                ('bio', models.CharField(help_text='Short bio for the chair', max_length=255)),
                ('bio_en', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('bio_fr', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('bio_es', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('bio_pt', models.CharField(help_text='Short bio for the chair', max_length=255, null=True)),
                ('image', models.ForeignKey(blank=True, help_text='Optional: image for the chair', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('item', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='chair_items', to='governance.MembersAssemblyPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]

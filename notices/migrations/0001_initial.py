# Generated by Django 2.2.9 on 2020-04-27 09:28

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_type', models.CharField(choices=[('notice', 'Notice (blue)'), ('alert', 'Alert (yellow)'), ('warning', 'Warning (red)')], default='notice', max_length=255)),
                ('content', wagtail.core.fields.RichTextField(help_text='Content for the notice')),
                ('content_en', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
                ('content_fr', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
                ('content_es', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
                ('content_pt', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_type', models.CharField(choices=[('notice', 'Notice (blue)'), ('alert', 'Alert (yellow)'), ('warning', 'Warning (red)')], default='notice', max_length=255)),
                ('content', wagtail.core.fields.RichTextField(help_text='Content for the notice')),
                ('content_en', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
                ('content_fr', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
                ('content_es', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
                ('content_pt', wagtail.core.fields.RichTextField(help_text='Content for the notice', null=True)),
                ('allow_dismiss', models.BooleanField(blank=True, default=False)),
                ('display_location', models.CharField(choices=[('all', 'All pages'), ('selected_page', 'Selected page only'), ('selected_page_and_children', 'Selected page and child pages'), ('children_only', 'Children of selected page')], default='selected_page', max_length=255)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
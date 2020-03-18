# Generated by Django 2.2.9 on 2020-03-02 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0003_member_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='constituency',
            field=models.ForeignKey(help_text='The constituency of the member', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to='taxonomies.Constituency'),
        ),
    ]
# Generated by Django 4.2.7 on 2024-01-07 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThesisListing', '0006_thesis_listings_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thesis_listings',
            old_name='field_name',
            new_name='accompanying_file',
        ),
    ]

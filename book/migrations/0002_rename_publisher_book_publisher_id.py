# Generated by Django 5.1.2 on 2024-11-20 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='publisher_id',
        ),
    ]

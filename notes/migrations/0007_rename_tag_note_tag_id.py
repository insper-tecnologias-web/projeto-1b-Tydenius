# Generated by Django 4.1.1 on 2022-09-14 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_note_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='tag',
            new_name='tag_id',
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-04 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0006_rename_trailer_desc_film_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='description',
            new_name='trailer_desc',
        ),
    ]
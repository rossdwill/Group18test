# Generated by Django 4.0.2 on 2022-02-17 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0004_rename_employee_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='employee_type',
            new_name='account_type',
        ),
    ]

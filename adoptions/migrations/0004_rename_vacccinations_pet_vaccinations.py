# Generated by Django 3.2.5 on 2021-07-10 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0003_rename_vacccination_pet_vacccinations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='vacccinations',
            new_name='vaccinations',
        ),
    ]

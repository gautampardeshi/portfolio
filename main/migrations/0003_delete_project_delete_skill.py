# Generated by Django 5.1.4 on 2024-12-22 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_created_at_contactmessage_submitted_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]

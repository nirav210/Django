# Generated by Django 3.1.6 on 2021-11-12 06:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='extendeduser',
            new_name='Profile',
        ),
    ]

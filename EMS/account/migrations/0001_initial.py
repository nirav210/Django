# Generated by Django 3.1.6 on 2021-10-24 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='extendeduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('designation', models.CharField(choices=[('Senior Web Developer', 'Senior Web Developer'), ('Junior Web Developer', 'Junior Web Developer'), ('Designer', 'Designer'), ('Tester', 'Tester')], default='Junior Web Developer', max_length=30, null=True)),
                ('salary', models.IntegerField()),
                ('bank_name', models.CharField(max_length=50)),
                ('account_number', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

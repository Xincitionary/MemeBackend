# Generated by Django 4.0.3 on 2022-03-31 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='post',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='post',
            new_name='id',
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_feed_options_alter_story_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feed',
            name='num_shares',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='story',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='story',
            name='num_shares',
            field=models.IntegerField(default=0),
        ),
    ]
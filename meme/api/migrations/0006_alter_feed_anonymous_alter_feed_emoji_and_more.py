# Generated by Django 4.0.3 on 2022-04-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_feed_num_likes_feed_num_shares_story_num_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='anonymous',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='feed',
            name='emoji',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='feed',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='anonymous',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='story',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]

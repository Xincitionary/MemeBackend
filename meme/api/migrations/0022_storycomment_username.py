# Generated by Django 3.2.8 on 2022-04-30 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_storycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='storycomment',
            name='username',
            field=models.CharField(blank=True, default='匿名', max_length=150, null=True),
        ),
    ]

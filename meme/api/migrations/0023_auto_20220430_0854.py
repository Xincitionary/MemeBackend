# Generated by Django 3.2.8 on 2022-04-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_storycomment_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storycomment',
            options={'ordering': ['-create_time']},
        ),
        migrations.AddField(
            model_name='storycomment',
            name='anonymous',
            field=models.BooleanField(blank=True, default=1),
        ),
    ]
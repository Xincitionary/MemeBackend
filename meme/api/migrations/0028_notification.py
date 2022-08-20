# Generated by Django 3.2.8 on 2022-05-30 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_userlogin_social_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_pic', models.IntegerField()),
                ('seen', models.BooleanField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=300)),
                ('Action', models.CharField(choices=[('LIKED', 'LIKED'), ('COMMENTED', 'COMMENTED'), ('REPLIED', 'REPLIED')], default='LIKED', max_length=10)),
                ('notifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userNotifying', to=settings.AUTH_USER_MODEL)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storyNotifying', to='api.story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userNotified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
    ]
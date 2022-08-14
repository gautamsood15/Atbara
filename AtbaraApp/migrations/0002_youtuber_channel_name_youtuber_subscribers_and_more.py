# Generated by Django 4.1 on 2022-08-14 12:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("AtbaraApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="youtuber",
            name="channel_name",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="youtuber",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True, related_name="subs", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="youtuber",
            name="youtubeimage",
            field=models.ImageField(default="", upload_to="ChannelPic"),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1 on 2022-08-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AtbaraApp", "0005_remove_video_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="Views",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
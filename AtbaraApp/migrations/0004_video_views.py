# Generated by Django 4.1 on 2022-08-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AtbaraApp", "0003_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="Views",
            field=models.IntegerField(default=""),
            preserve_default=False,
        ),
    ]
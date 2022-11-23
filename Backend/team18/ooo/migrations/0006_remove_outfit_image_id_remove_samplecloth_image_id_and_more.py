# Generated by Django 4.1.1 on 2022-11-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ooo", "0005_remove_samplecloth_outfit_alter_usercloth_dates_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="outfit", name="image_id",),
        migrations.RemoveField(model_name="samplecloth", name="image_id",),
        migrations.RemoveField(model_name="usercloth", name="image_id",),
        migrations.AddField(
            model_name="outfit",
            name="image_link",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="samplecloth",
            name="image_link",
            field=models.CharField(default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="usercloth",
            name="image_link",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
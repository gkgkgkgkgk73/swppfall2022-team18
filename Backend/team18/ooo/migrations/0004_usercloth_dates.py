# Generated by Django 4.1.1 on 2022-11-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ooo", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="usercloth",
            name="dates",
            field=models.TextField(default='"[]"'),
        ),
    ]

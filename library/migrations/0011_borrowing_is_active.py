# Generated by Django 4.1.7 on 2023-02-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0010_rename_book_id_borrowing_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowing",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
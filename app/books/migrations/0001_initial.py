# Generated by Django 5.1 on 2025-01-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True,
                        help_text="Book title",
                        max_length=64,
                        unique=True,
                    ),
                ),
                ("description", models.TextField(help_text="Book title")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Book creation date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Book update date"),
                ),
            ],
        ),
    ]

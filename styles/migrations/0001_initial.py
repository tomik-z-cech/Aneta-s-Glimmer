# Generated by Django 4.2.7 on 2023-12-08 18:21

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StylesAvailable",
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
                ("style_name", models.CharField(max_length=100)),
                ("style_description", models.TextField()),
                (
                    "sample_image",
                    cloudinary.models.CloudinaryField(
                        default="default_sample_image",
                        max_length=255,
                        verbose_name="image",
                    ),
                ),
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="style_likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "want_to_try",
                    models.ManyToManyField(
                        blank=True,
                        related_name="want_to_try",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Available Style",
            },
        ),
        migrations.CreateModel(
            name="StylesComments",
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
                ("username", models.CharField(max_length=80)),
                ("comment_body", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("approved", models.BooleanField(default=False)),
                (
                    "style",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="style_comments",
                        to="styles.stylesavailable",
                    ),
                ),
            ],
            options={
                "verbose_name": "Style Comment",
                "ordering": ["created_on"],
            },
        ),
    ]

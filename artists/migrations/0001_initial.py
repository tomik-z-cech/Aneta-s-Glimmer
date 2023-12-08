# Generated by Django 4.2.7 on 2023-12-08 18:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("styles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Artists",
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
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "profile_picture",
                    cloudinary.models.CloudinaryField(
                        default="default_artist_pp",
                        max_length=255,
                        verbose_name="image",
                    ),
                ),
                ("bio", models.TextField()),
                ("public_profile", models.URLField()),
                ("start_date", models.DateField()),
                ("rating", models.FloatField(default=5.0)),
                ("bookings_total", models.PositiveIntegerField(default=0)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("styles", models.ManyToManyField(to="styles.stylesavailable")),
            ],
            options={
                "verbose_name": "Artist",
            },
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-08 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("artists", "0001_initial"),
        ("bookings", "0015_alter_newscomments_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newscomments",
            name="post",
        ),
        migrations.RemoveField(
            model_name="newscomments",
            name="username",
        ),
        migrations.RemoveField(
            model_name="newsposts",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="newsposts",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="stylesavailable",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="stylesavailable",
            name="want_to_try",
        ),
        migrations.RemoveField(
            model_name="stylescomments",
            name="style",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.AlterField(
            model_name="bookings",
            name="booked_artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="booking",
                to="artists.artists",
            ),
        ),
        migrations.DeleteModel(
            name="Artists",
        ),
        migrations.DeleteModel(
            name="NewsComments",
        ),
        migrations.DeleteModel(
            name="NewsPosts",
        ),
        migrations.DeleteModel(
            name="StylesAvailable",
        ),
        migrations.DeleteModel(
            name="StylesComments",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]

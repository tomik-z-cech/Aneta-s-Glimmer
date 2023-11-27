# Generated by Django 4.2.7 on 2023-11-27 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0014_alter_userprofile_marketing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscomments',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]

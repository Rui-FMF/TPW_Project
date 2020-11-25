# Generated by Django 3.1 on 2020-11-25 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_article_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articles_bought', to=settings.AUTH_USER_MODEL),
        ),
    ]

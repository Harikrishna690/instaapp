# Generated by Django 2.2.4 on 2019-08-23 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('themainapp', '0005_auto_20190822_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='person_uploaded',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
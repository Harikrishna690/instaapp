# Generated by Django 2.2.4 on 2019-08-22 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('themainapp', '0002_auto_20190822_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked',
            name='personId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
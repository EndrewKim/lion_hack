# Generated by Django 2.1.8 on 2019-08-05 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my.homepage', '0002_auto_20190804_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='center_image',
            field=models.URLField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
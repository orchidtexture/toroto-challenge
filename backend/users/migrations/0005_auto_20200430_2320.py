# Generated by Django 2.2 on 2020-04-30 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200430_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptor',
            name='user',
        ),
        migrations.AddField(
            model_name='subscriptor',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscriptor',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.4 on 2021-01-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210106_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_full_name_displayed',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
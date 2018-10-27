# Generated by Django 2.1.1 on 2018-10-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolerp', '0008_auto_20181021_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='name',
        ),
        migrations.AddField(
            model_name='classroom',
            name='section',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='classroom',
            name='standard',
            field=models.IntegerField(null=True),
        ),
    ]
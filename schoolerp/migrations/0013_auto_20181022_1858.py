# Generated by Django 2.1.1 on 2018-10-22 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolerp', '0012_auto_20181021_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='evaluated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolerp.Profile'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teachermark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_test', models.CharField(max_length=200)),
                ('classteacher', models.CharField(max_length=200)),
                ('standard', models.IntegerField()),
                ('section', models.CharField(max_length=1)),
                ('studentname', models.CharField(max_length=25)),
                ('maxtestmarks', models.IntegerField()),
                ('marks_obtained', models.IntegerField()),
                ('studentpercentage', models.FloatField()),
            ],
        ),
    ]

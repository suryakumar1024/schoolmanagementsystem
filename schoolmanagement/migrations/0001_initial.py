# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staff_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(max_length=50)),
                ('year_of_class', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tamil', models.IntegerField()),
                ('telugu', models.IntegerField()),
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('science', models.IntegerField()),
                ('social', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='subjects',
            field=models.OneToOneField(to='schoolmanagement.Subjects'),
        ),
        migrations.AddField(
            model_name='staff',
            name='classes',
            field=models.ManyToManyField(to='schoolmanagement.Subjects'),
        ),
    ]

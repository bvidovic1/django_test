# Generated by Django 2.1.7 on 2019-02-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('link', models.URLField(verbose_name='Advertisement Link')),
                ('company', models.CharField(max_length=140)),
                ('year', models.IntegerField()),
                ('engine_type', models.CharField(choices=[('b', 'Benzin'), ('d', 'Diesel')], max_length=1)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.URLField()),
                ('download_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

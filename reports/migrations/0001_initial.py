# Generated by Django 2.2.6 on 2019-10-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0)),
                ('descripttion', models.TextField()),
                ('lawyer', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]

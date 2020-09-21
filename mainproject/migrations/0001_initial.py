# Generated by Django 2.2.5 on 2019-09-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urlhacked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=256)),
                ('short_url', models.CharField(max_length=8, unique=True)),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
            ],
        ),
    ]

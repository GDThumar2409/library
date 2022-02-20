# Generated by Django 3.0.1 on 2020-01-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_no', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]

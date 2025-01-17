# Generated by Django 5.1 on 2024-09-01 20:15

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('color', multiselectfield.db.fields.MultiSelectField(choices=[('blck', 'Black'), ('wht', 'White'), ('bl', 'Blue'), ('rd', 'Red'), ('yllw', 'Yellow'), ('gry', 'Grey'), ('grn', 'Green')], max_length=27)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]

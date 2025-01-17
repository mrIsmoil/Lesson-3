# Generated by Django 5.1 on 2024-09-04 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-23 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.2 on 2022-01-19 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-modified_at']},
        ),
    ]

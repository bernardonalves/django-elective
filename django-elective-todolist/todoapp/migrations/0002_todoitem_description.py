# Generated by Django 2.2.5 on 2019-09-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

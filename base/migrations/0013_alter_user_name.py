# Generated by Django 4.1.5 on 2023-03-31 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]

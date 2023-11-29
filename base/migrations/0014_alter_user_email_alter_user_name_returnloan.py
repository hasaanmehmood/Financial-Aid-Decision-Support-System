# Generated by Django 4.1.5 on 2023-05-15 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0013_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.CreateModel(
            name='ReturnLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transationmode', models.CharField(max_length=15)),
                ('transactionid', models.CharField(max_length=15)),
                ('transactiondate', models.DateField()),
                ('transactionamount', models.IntegerField()),
                ('transactionreceipt', models.FileField(default='transactionreceipt/default.pdf', upload_to='transactionreceipt')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
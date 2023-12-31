# Generated by Django 4.1.5 on 2023-01-07 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('role', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DecisionMaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('cnic', models.CharField(max_length=14)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSC_Result', models.IntegerField(max_length=4)),
                ('HSSC_Result', models.IntegerField(max_length=4)),
                ('Father_NTN', models.CharField(max_length=25)),
                ('UtilityBill', models.IntegerField()),
                ('Income', models.IntegerField()),
                ('Expenses', models.IntegerField()),
                ('Property_Area', models.IntegerField()),
                ('Description', models.CharField(max_length=500)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll', models.CharField(max_length=7)),
                ('fathername', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=11)),
                ('cnic', models.CharField(max_length=14)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.user'),
        ),
    ]

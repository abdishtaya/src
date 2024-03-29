# Generated by Django 2.1 on 2019-06-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('username', models.CharField(max_length=255, verbose_name='username')),
                ('password', models.CharField(max_length=255, verbose_name='pass')),
                ('active', models.CharField(max_length=10, verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='username')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('type', models.CharField(max_length=255, verbose_name='type')),
                ('password', models.CharField(max_length=10, verbose_name='pass')),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_employees', models.CharField(max_length=255, verbose_name='email_employees')),
                ('email_customers', models.CharField(max_length=255, verbose_name='email_customers')),
                ('name_service', models.CharField(max_length=255, verbose_name='name_service')),
                ('active', models.CharField(max_length=10, verbose_name='active')),
            ],
        ),
    ]

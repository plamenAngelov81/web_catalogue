# Generated by Django 4.1.3 on 2022-12-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0003_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('message', models.TextField(verbose_name='Your message')),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0026_auto_20211102_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=12, unique=True, verbose_name='Телефон'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0024_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(editable=False, max_length=12, verbose_name='Телефон'),
        ),
    ]

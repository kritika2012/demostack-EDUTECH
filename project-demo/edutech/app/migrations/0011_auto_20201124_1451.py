# Generated by Django 3.1.1 on 2020-11-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201124_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
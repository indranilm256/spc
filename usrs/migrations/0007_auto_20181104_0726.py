# Generated by Django 2.1.2 on 2018-11-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrs', '0006_auto_20181104_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

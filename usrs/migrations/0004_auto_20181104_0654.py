# Generated by Django 2.1.2 on 2018-11-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usrs', '0003_auto_20181103_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
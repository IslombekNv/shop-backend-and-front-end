# Generated by Django 3.2 on 2021-05-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brandmodel_productmodel_producttagmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttagmodel',
            options={'verbose_name': 'producttag', 'verbose_name_plural': 'producttags'},
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]

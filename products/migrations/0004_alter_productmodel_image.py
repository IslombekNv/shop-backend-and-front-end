# Generated by Django 3.2 on 2021-05-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210504_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]

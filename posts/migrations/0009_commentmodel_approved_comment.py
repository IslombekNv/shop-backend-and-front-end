# Generated by Django 3.2 on 2021-05-24 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_commentmodel_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]

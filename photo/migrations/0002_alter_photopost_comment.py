# Generated by Django 4.2 on 2024-11-25 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photopost',
            name='comment',
            field=models.TextField(verbose_name='コメント'),
        ),
    ]

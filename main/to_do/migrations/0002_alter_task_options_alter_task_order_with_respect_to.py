# Generated by Django 4.1.3 on 2023-01-05 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]

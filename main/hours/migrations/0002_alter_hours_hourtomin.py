# Generated by Django 4.1.3 on 2023-02-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='hourtomin',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
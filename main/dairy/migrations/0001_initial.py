# Generated by Django 4.1.3 on 2023-03-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dairy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='write something my boi', max_length=200)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
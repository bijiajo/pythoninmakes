# Generated by Django 4.2.2 on 2023-07-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1990-05-12'),
            preserve_default=False,
        ),
    ]

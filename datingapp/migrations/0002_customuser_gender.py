# Generated by Django 4.2.5 on 2023-09-22 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('М', 'Студент'), ('Ж', 'Студентка')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]

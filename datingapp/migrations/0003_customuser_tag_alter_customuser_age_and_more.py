# Generated by Django 4.2.5 on 2023-09-22 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datingapp', '0002_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tag',
            field=models.TextField(blank=True, verbose_name='Тег в телеграмме'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('М', 'Студент'), ('Ж', 'Студентка')], max_length=1, verbose_name='Пол'),
        ),
    ]

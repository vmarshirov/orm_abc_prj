# Generated by Django 4.1.7 on 2023-03-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_abc_app', '0007_alter_abc_c'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abc',
            options={'ordering': ('a', '-b'), 'verbose_name': 'A_B_C', 'verbose_name_plural': 'A_B_C_S'},
        ),
        migrations.AlterField(
            model_name='abc',
            name='b',
            field=models.IntegerField(default=0, help_text='Подсказка для поля', verbose_name='Значение B'),
        ),
        migrations.AlterField(
            model_name='abc',
            name='c',
            field=models.IntegerField(choices=[(0, 'ноль'), (10, 'десять'), (15, 'пятнадцать'), (20, 'двадцать')], default=0, verbose_name='Значение С'),
        ),
    ]

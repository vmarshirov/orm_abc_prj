# Generated by Django 4.1.7 on 2023-02-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='Равна ли С сумме A и B ?', max_length=256, verbose_name='Формулировка задачи')),
                ('a', models.IntegerField(default=0, verbose_name='Значение А')),
                ('b', models.IntegerField(default=0, verbose_name='Значение B')),
                ('c', models.IntegerField(choices=[(0, 'ноль'), (10, 'десять'), (15, 'пятьнадцать'), (20, 'двадцать')], default=0, verbose_name='Значение С')),
                ('current_date', models.DateTimeField(auto_now=True, verbose_name='Дата Записи')),
                ('upload', models.FileField(blank=True, null=True, upload_to='item_images/', verbose_name='Загружен файл')),
            ],
            options={
                'verbose_name': 'A_B_C',
                'verbose_name_plural': 'A_B_C_S',
                'ordering': ('-c', 'b'),
            },
        ),
    ]

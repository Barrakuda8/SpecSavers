# Generated by Django 5.0.6 on 2024-05-21 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=128, verbose_name='Модель')),
                ('cores', models.SmallIntegerField(verbose_name='Количество ядер')),
                ('frequency', models.IntegerField(verbose_name='Частота процессора (МГц)')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64, verbose_name='Производитель')),
                ('model', models.CharField(max_length=128, verbose_name='Модель')),
                ('weight', models.IntegerField(verbose_name='Вес (г)')),
                ('diagonal', models.FloatField(verbose_name='Диагональ экрана (дюйм)')),
                ('resolution_width', models.IntegerField(verbose_name='Разрешение экрана - Ширина')),
                ('resolution_height', models.IntegerField(verbose_name='Разрешение экрана - Высота')),
                ('price', models.IntegerField(verbose_name='Стоимость (Лей)')),
                ('link', models.TextField(verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Изображение')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=128, verbose_name='Модель')),
                ('rank', models.IntegerField(verbose_name='Показатель сравнения')),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.device')),
                ('memory', models.FloatField(blank=True, null=True, verbose_name='Встроенная память (Гб)')),
                ('battery', models.IntegerField(verbose_name='Аккамуляторная батарея (мАч)')),
            ],
            bases=('main.device',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.device')),
                ('memory', models.IntegerField(verbose_name='Встроенная память (Гб)')),
                ('ram', models.IntegerField(verbose_name='Оперативная память (Гб)')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cpu', verbose_name='Процессор')),
                ('video_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.videocard', verbose_name='Видеокарта')),
            ],
            bases=('main.device',),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.device')),
                ('memory', models.IntegerField(verbose_name='Встроенная память (Гб)')),
                ('ram', models.IntegerField(verbose_name='Оперативная память (Гб)')),
                ('main_camera', models.IntegerField(verbose_name='Основная камера (Мп)')),
                ('front_camera', models.IntegerField(verbose_name='Фронтальная камера (Мп)')),
                ('battery', models.IntegerField(verbose_name='Аккамуляторная батарея (мАч)')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cpu', verbose_name='Процессор')),
            ],
            bases=('main.device',),
        ),
    ]

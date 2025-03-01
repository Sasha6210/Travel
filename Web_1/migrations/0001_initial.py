# Generated by Django 4.2.2 on 2024-06-03 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=15)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kid_age', models.IntegerField(help_text='Вік учня', null=True, verbose_name='Вік учня')),
                ('price', models.IntegerField(help_text='Вкажіть вартість', null=True, verbose_name='Вартість')),
                ('data_price', models.IntegerField(verbose_name='Дата')),
                ('image', models.TextField(verbose_name='Картинка')),
                ('description', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Web_1.category', verbose_name='Категорія курсу')),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2024-06-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_1', '0003_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 4.0.5 on 2022-09-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacciresult',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]

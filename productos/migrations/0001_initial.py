# Generated by Django 5.1.1 on 2024-10-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('unidades', models.IntegerField(blank=True)),
            ],
        ),
    ]

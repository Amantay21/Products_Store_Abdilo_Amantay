# Generated by Django 5.0 on 2024-01-03 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_product_image_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.PositiveIntegerField(default=1, verbose_name='Остаток'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='webapp.product', verbose_name='Продукт')),
            ],
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-21 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]

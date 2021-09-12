# Generated by Django 3.2 on 2021-07-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=150, verbose_name='Customer')),
                ('description', models.TextField(max_length=5000, verbose_name='Order description')),
            ],
            options={
                'verbose_name': 'Order',
            },
        ),
    ]

# Generated by Django 5.1 on 2024-09-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bistroapp', '0009_delete_chef_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('chefimg', models.ImageField(upload_to='chef/')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='menu/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

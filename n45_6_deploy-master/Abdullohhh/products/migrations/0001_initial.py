# Generated by Django 5.0.7 on 2024-07-21 18:36

import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('image', models.ImageField(upload_to='products/category/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='products/product/')),
                ('description', markdownx.models.MarkdownxField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('massa', models.CharField(choices=[('kg', 'Kg'), ('mg', 'Mg'), ('lg', 'Lg'), ('pc', 'Piece')], default='kg', max_length=4)),
                ('count', models.PositiveIntegerField(default=1)),
                ('rating', models.FloatField(blank=True, default=0, null=True)),
                ('status', models.CharField(choices=[('pb', 'Publish'), ('df', 'Draft')], default='pb', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='products.category')),
            ],
        ),
    ]

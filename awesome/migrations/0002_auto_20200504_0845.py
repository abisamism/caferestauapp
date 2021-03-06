# Generated by Django 3.0.5 on 2020-05-04 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awesome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'about us ',
                'verbose_name_plural': 'about us ',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='chef/')),
            ],
            options={
                'verbose_name': 'chef',
                'verbose_name_plural': 'chef',
            },
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('people', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('preperation_time', models.IntegerField()),
                ('image', models.ImageField(upload_to='meals/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awesome.Category')),
            ],
            options={
                'verbose_name': 'meal',
                'verbose_name_plural': 'meals',
            },
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-18 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('deadline', models.DateField()),
                ('description', models.TextField()),
                ('picture1', models.ImageField(upload_to='media')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='media')),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.type')),
            ],
        ),
    ]

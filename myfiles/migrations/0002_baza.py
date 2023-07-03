# Generated by Django 4.2.2 on 2023-06-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture1', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=50)),
                ('deadline', models.DateField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
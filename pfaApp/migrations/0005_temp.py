# Generated by Django 4.2 on 2023-05-04 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfaApp', '0004_pression'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(null=True)),
                ('dt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
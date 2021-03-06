# Generated by Django 3.2.6 on 2022-02-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20220210_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]

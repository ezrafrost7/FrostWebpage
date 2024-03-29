# Generated by Django 3.1.2 on 2021-08-01 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AAPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Negative', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Neutral', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Positive', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Compound', models.DecimalField(decimal_places=2, max_digits=4)),
                ('StockOpen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockHigh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockLow', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockClose', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Negative', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Neutral', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Positive', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Compound', models.DecimalField(decimal_places=2, max_digits=4)),
                ('StockOpen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockHigh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockLow', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockClose', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TSLA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Negative', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Neutral', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Positive', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Compound', models.DecimalField(decimal_places=2, max_digits=4)),
                ('StockOpen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockHigh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockLow', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockClose', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

# Generated by Django 2.0.3 on 2019-05-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.0.3 on 2019-05-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderapp', '0003_remove_place_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='flag',
            field=models.CharField(default='visited', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]
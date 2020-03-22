# Generated by Django 3.0.3 on 2020-02-23 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0002_wine_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='restaurants',
        ),
        migrations.AddField(
            model_name='wine',
            name='restaurants',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='wine.Restaurants'),
            preserve_default=False,
        ),
    ]

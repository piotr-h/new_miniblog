# Generated by Django 3.0.7 on 2020-07-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200703_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edited_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data edycji'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200703_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edited_date',
            field=models.DateTimeField(null=True, verbose_name='Data edycji'),
        ),
    ]
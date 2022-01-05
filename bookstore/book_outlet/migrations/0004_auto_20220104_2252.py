# Generated by Django 3.2.9 on 2022-01-04 22:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='family',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='family',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)]),
        ),
    ]
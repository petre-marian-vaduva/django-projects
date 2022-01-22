# Generated by Django 3.2.9 on 2022-01-22 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0005_auto_20220120_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='name',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_outlet.address'),
        ),
    ]
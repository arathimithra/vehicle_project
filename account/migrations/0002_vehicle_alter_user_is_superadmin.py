# Generated by Django 4.2.4 on 2023-08-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(blank=True, max_length=200, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=200, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=500, null=True)),
                ('vehicle_description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superadmin',
            field=models.BooleanField(default=False, verbose_name='Is superadmin'),
        ),
    ]

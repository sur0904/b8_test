# Generated by Django 4.1.4 on 2023-02-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='lcreateddate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

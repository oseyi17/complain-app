# Generated by Django 3.2.13 on 2022-06-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0003_complain_treated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
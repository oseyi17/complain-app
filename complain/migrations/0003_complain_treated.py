# Generated by Django 3.2.13 on 2022-06-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0002_auto_20220608_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='treated',
            field=models.BooleanField(default=False),
        ),
    ]
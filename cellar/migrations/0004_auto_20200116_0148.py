# Generated by Django 3.0.2 on 2020-01-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0003_auto_20200116_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottle',
            name='Image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

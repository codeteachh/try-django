# Generated by Django 4.2 on 2023-04-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
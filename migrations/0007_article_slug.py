# Generated by Django 4.2 on 2023-04-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles2', '0006_alter_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

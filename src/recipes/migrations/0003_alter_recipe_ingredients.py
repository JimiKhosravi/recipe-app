# Generated by Django 4.1.7 on 2023-03-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(help_text='Ingredients must be separated by commas.', max_length=350),
        ),
    ]

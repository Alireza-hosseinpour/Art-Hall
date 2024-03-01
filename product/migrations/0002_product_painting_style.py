# Generated by Django 5.0.2 on 2024-03-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='painting_style',
            field=models.CharField(choices=[('acrylic', 'acrylic'), ('oil', 'oil'), ('water-color', 'water-color'), ('gouache', 'gouache'), ('digital-painting', 'digital-painting'), ('pastel', 'pastel'), ('other', 'other')], default='other', max_length=20),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-22 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='exemplo_upload',
            field=models.FileField(blank=True, null=True, upload_to='outro_diretorio/'),
        ),
    ]

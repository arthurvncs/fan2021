# Generated by Django 3.1.7 on 2021-03-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20210329_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email_cliente',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-29 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nft_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nft',
            options={'ordering': ('-creation_date',)},
        ),
        migrations.RenameField(
            model_name='nft',
            old_name='descritption',
            new_name='description',
        ),
    ]
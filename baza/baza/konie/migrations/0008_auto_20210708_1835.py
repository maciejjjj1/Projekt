# Generated by Django 3.2.3 on 2021-07-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konie', '0007_alter_ocena_kon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ocena',
            options={'ordering': ('kon', 'ocena')},
        ),
        migrations.AddField(
            model_name='ocena',
            name='ocena',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]

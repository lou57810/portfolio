# Generated by Django 5.0.6 on 2024-09-10 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0006_alter_todoitems_item_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitems',
            old_name='item_name',
            new_name='TODO',
        ),
    ]

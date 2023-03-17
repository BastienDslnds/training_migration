# Generated by Django 4.1.7 on 2023-03-17 08:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sale", "0002_alter_sale_product"),
        ("catalog", "0002_remove_product_category"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Product',
                ),
            ],
            # You want to reuse the table, so don't drop it
            database_operations=[],
        ),
    ]

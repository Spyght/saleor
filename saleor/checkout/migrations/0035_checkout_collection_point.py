# Generated by Django 3.2.2 on 2021-07-09 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0015_auto_20210709_1454"),
        ("checkout", "0034_remove_checkout_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="collection_point",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="checkouts",
                to="warehouse.warehouse",
            ),
        ),
    ]

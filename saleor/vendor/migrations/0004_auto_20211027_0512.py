# Generated by Django 3.2.7 on 2021-10-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0120_orderline_optional_sku"),
        ("vendor", "0003_vendor_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="allocation",
        ),
        migrations.AddField(
            model_name="vendor",
            name="order",
            field=models.ManyToManyField(related_name="vendor_order", to="order.Order"),
        ),
    ]

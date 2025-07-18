# Generated by Django 3.2.25 on 2025-07-10 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0006_medicine_suppliers'),
        ('medicine_request', '0002_alter_supplier_managed_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinerequest',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.medicine'),
        ),
        migrations.AlterField(
            model_name='suppliermedicine',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_management.medicine'),
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
    ]

# Generated by Django 3.2.18 on 2023-05-10 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0010_remove_expense_expense_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='expense_account',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.account'),
            preserve_default=False,
        ),
    ]

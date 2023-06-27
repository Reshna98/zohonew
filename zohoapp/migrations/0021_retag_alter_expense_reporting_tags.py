# Generated by Django 4.2.2 on 2023-06-27 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0020_alter_expense_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='retag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporting_tags', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='reporting_tags',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.retag'),
            preserve_default=False,
        ),
    ]

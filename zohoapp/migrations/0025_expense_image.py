# Generated by Django 4.2.2 on 2023-06-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0024_remove_expense_attachment_attach'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='expense_image/'),
        ),
    ]

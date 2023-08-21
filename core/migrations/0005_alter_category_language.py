# Generated by Django 4.2.4 on 2023-08-17 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.language'),
        ),
    ]

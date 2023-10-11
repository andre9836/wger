# Generated by Django 4.1.9 on 2023-09-27 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('nutrition', '0016_alter_logitem_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutritionplan',
            name='language',
        ),
        migrations.AlterField(
            model_name='logitem',
            name='meal',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='log_items',
                to='nutrition.meal',
                verbose_name='Meal'
            ),
        ),
        migrations.AddField(
            model_name='nutritionplan',
            name='only_logging',
            field=models.BooleanField(default=False, verbose_name='Only logging'),
        ),
    ]

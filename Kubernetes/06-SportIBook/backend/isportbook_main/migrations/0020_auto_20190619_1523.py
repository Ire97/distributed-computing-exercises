# Generated by Django 2.2.1 on 2019-06-19 15:23

from django.db import migrations
import isportbook_main.models.models_utils.integer_range_field


class Migration(migrations.Migration):

    dependencies = [
        ('isportbook_main', '0019_auto_20190617_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='closeness',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='punctuality',
        ),
        migrations.AddField(
            model_name='feedback',
            name='motivation',
            field=isportbook_main.models.models_utils.integer_range_field.IntegerRangeField(default=0, verbose_name='Motivation'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='professionality',
            field=isportbook_main.models.models_utils.integer_range_field.IntegerRangeField(default=0, verbose_name='Professionality'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='cleaning',
            field=isportbook_main.models.models_utils.integer_range_field.IntegerRangeField(default=0, verbose_name='Cleaning'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='passion',
            field=isportbook_main.models.models_utils.integer_range_field.IntegerRangeField(default=0, verbose_name='Passion'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='skill',
            field=isportbook_main.models.models_utils.integer_range_field.IntegerRangeField(default=0, verbose_name='Skill'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='value_for_money',
            field=isportbook_main.models.models_utils.integer_range_field.IntegerRangeField(default=0, verbose_name='Value for money'),
        ),
    ]
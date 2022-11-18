# Generated by Django 4.1.2 on 2022-11-14 20:50

from django.db import migrations, models
import quiz.validators


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='order_num',
            field=models.PositiveSmallIntegerField(validators=[quiz.validators.order_num_count]),
        ),
    ]

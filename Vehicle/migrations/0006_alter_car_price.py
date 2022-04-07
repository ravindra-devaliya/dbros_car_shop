# Generated by Django 4.0.3 on 2022-03-29 04:02

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0005_alter_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('1000'), default_currency='USD', help_text='$1000 - $100,000', max_digits=6, validators=[djmoney.models.validators.MinMoneyValidator(1000), djmoney.models.validators.MaxMoneyValidator(100000)], verbose_name='Asking Price'),
        ),
    ]
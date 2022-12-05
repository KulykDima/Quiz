from django.core.exceptions import ValidationError


def order_num_count(values):
    if 1 > values > 100:
        raise ValidationError('Order num is only in range from 1 to 100!')

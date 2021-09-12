# Create your tasks here

import time

from celery import shared_task
from utils import send_email


@shared_task
def cook_pizza(email, customer):
    time.sleep(80)
    message = 'Hey {}! \n\n Your pizza is cooked!'.format(customer)
    send_email('Pizza cooked!', message, [email])
    return 'Pizza cooked!'

@shared_task
def bill(email, customer):
    time.sleep(40)
    message = 'Hello {}! \n\n Your pizza billing is ok!'.format(customer)
    send_email('Pizza cooked!', message, [email])
    return 'Billing ok!'


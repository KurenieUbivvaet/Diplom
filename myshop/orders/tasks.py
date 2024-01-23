from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    '''
    Задача для отправки уведомлений по электронной почте при успешном создании заказа.
    '''
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа {}'.format(order_id)
    message = 'Здравствуйте, {} {}, \n\nВы успешно оформили заказ.\nНомер вашего заказа {}'.format(order.name,
                                                                                                   order.patronymic,
                                                                                                   order.id)
    mail_sent =send_mail(subject, message, 'admin@betonit.com', [order.email])
    return mail_sent
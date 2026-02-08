from __future__ import annotations
from celery import shared_task
from config.celery import app as celery_app
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@celery_app.task(bind=True, name='apps.orders.tasks.notify_supplier')
def notify_supplier_task(self, order_id: int):
    """Celery task to notify supplier about a new order."""
    try:
        # Импорт модели внутри задачи, чтобы избежать проблем при старте воркера
        from apps.orders.models import Order
        order = Order.objects.select_related('user').prefetch_related('ordered_items').get(id=order_id)
        subject = f'New order #{order.id}'
        message = f'Order {order.id} created for user {order.user.email}'
        recipient_list = [settings.DEFAULT_FROM_EMAIL]
        # Здесь должен быть реальный адрес поставщика; для простоты используем DEFAULT_FROM_EMAIL
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
        logger.info('Notified supplier about order %s', order_id)
    except Order.DoesNotExist:
        logger.exception('Order not found: %s', order_id)
    except Exception:
        logger.exception('Failed to notify supplier for order %s', order_id)

# Пример простой задачи для отладки
@shared_task
def add(x, y):
    return x + y

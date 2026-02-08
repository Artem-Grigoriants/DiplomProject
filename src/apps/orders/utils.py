def notify_supplier_sync(order_id: int):
    """
    Заглушка для синхронного уведомления поставщика о заказе.
    В реальном проекте здесь будет HTTP запрос к API поставщика или отправка сообщения.
    Сейчас просто логируем (print) для тестов и предотвращения ошибок импорта.
    """
    print(f"notify_supplier_sync called for order {order_id}")
    return True


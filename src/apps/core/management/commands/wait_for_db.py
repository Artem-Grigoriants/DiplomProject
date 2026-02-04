#Файл `wait_for_db.py` — это пользовательская команда управления Django.
#Её цель — убедиться в доступности базы данных до запуска приложения.
#Она постоянно пытается установить соединение с базой данных,
#повторяя попытку каждую секунду, пока соединение не будет установлено успешно.
from time import sleep
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Wait for the database to be available'

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                db_conn.cursor()
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
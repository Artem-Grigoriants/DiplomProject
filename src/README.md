Краткое руководство по запуску и тестированию проекта
===============================================

Предусловия
-----------
- Docker и Docker Compose установлены (или Docker Desktop).
- Для локального запуска: Python 3.10+, virtualenv.

Запуск через Docker (рекомендуется)
----------------------------------
1) Перейдите в каталог с `docker-compose.yml`:

```bash
cd /mnt/c/python/Project/Netoligy/My_diplom/project/src
```

2) Остановить и удалить старые контейнеры (и тома при необходимости):

```bash
# Остановить и удалить контейнеры (без удаления томов)
docker compose down --remove-orphans

# Если нужны полностью чистая БД и тома (данные будут удалены):
docker compose down -v --remove-orphans
```

3) Сборка и запуск в фоне:

```bash
docker compose up --build -d
```

4) Просмотр логов (в реальном времени):

```bash
docker compose logs -f web
```

5) Создание суперпользователя (интерактивно):

```bash
docker compose exec web python manage.py createsuperuser --email you@domain.tld
```

6) Запуск тестов внутри контейнера:

```bash
# Один раз (в отдельном контейнере)
docker compose run --rm web python manage.py test --verbosity=2
```

Локальный запуск без Docker
---------------------------
1) Создайте и активируйте виртуальное окружение (пример для Unix/WSL):

```bash
python -m venv venv
source venv/bin/activate
```

2) Установите зависимости:

```bash
pip install -r requirements.txt
```

3) Проверьте настройки БД в `src/config/settings.py` и запустите миграции:

```bash
cd src
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

4) Создание суперпользователя локально:

```bash
python manage.py createsuperuser --email you@domain.tld
```

Запуск тестов локально
----------------------
```bash
# в активированном venv, в папке src
python manage.py test
```

Полезные команды Docker
-----------------------
```bash
# Статус контейнеров
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Логи конкретного сервиса
docker compose logs --tail=200 web

# Выполнение команды внутри контейнера (например, shell)
docker compose exec web sh
```

Советы и замечания
------------------
- В Docker настройки БД берутся из переменных окружения, хост базы внутри compose — `db`.
- Если база в контейнере содержит артефакты от старых запусков, очистите том `postgres_data` командой `docker compose down -v`.
- Для автоматизации CI используйте `docker compose run --rm web python manage.py test`.

Если хотите, могу положить краткую версию в корень репозитория или расширить README инструкциями по деплою/CI.

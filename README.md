# 19ad8ec7231e0cc9d9ea7e0684742672018e1f05
Тестовое задание

Сперва зайдите в папку с файлом manage.py и создайте там виртуальную среду с помощью:
```diff
> python -m venv Venv
```

Дождитесь создания виртуальной среды, а затем активируйте:
> Venv\Scripts\activate

Затем установите python зависимсти для проекта:
> pip install -r requirements.txt

После установки, поднимитесь в каталог выше где находится docker-compose.yml файл и поднимите экосистему для проекта
(PostgreSQL, Highcharts, RabbitMQ, Redis):
> docker-compose up

Затем перейдите в другой терминал, снова активируйте виртуальную среду и запустите из папки с файлом manage.py:
> celery -A FunctionModeler worker -l info --pool=solo
Так мы запустим Celery worker, он сразу должен подключиться к Redis и RabbitMQ.

Тажке оставим этот терминал, и поднимем сервер для приложения в другом терминале, не забывая использовать Venv:
python manage.py runserver

Заходим на http://127.0.0.1:8000/ в браузере и проверяем работу!

import os
import time

import json
import requests
import pyparsing
from datetime import datetime
from datetime import timedelta
from .fourFN import NumericStringParser
from django.conf import settings


def get_chart_image(chart_id, expression, day_interval, dt):
    """
    Функция рендерит изображение графика по полученным данным, а затем возвращает время завершения и путь к изображению
    """
    xAxis = []
    yAxis = []
    interval = timedelta(days=day_interval)  # Интервал в днях
    start_time = datetime.now() - interval
    end_time = datetime.now()
    time_diff = int(((end_time - start_time).days * 24) / dt)

    for i in range(time_diff):
        start_time += timedelta(hours=dt)
        xAxis.append(int(time.mktime(start_time.timetuple())))

    # Проверяем верно ли математическое выражение введённое пользователем, заполняя массив для оси абсцисс графика
    nsp_ = NumericStringParser()
    for i in xAxis:
        try:
            result_ = nsp_.safe_eval(expression.replace('t', str(i)))
        except pyparsing.ParseException:
            result_ = "Error"
        yAxis.append(result_)

    # Формируем точки для графика
    DATA = [list(l) for l in zip(xAxis, yAxis)]

    headers = {'Content-Type': 'application/json', }

    data = {
        "infile":
            {
                "title": {"text": 'Chart of y=' + expression + ' function'},
                "offset": -max(xAxis),
                "series": [{"data": DATA, "name": 'y=' + expression}]
            }
    }

    data = json.dumps(data)
    response = requests.post('http://127.0.0.1:8889', headers=headers, data=data)
    path = os.path.join(f'{settings.MEDIA_ROOT}', 'media', f'{chart_id}_chart.png')
    with open(path, 'wb') as out_file:
        out_file.write(response.content)
    return tuple([f'media/{chart_id}_chart.png', datetime.now().strftime("%m-%d-%Y %H:%M:%S")])

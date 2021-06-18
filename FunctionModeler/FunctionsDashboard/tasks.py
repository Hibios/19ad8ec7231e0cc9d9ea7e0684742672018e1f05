from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .services import get_chart_image


@shared_task
def generate_image(chart_id, expression, day_interval, dt):
    return get_chart_image(chart_id, expression, day_interval, dt)

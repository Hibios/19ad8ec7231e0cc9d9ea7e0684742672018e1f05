from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import mark_safe
from .tasks import generate_image


class Chart(models.Model):
    chart_id = models.AutoField(primary_key=True)
    chart_function = models.CharField(max_length=40)
    chart_interval = models.IntegerField(null=False)
    chart_step = models.IntegerField(null=False)
    chart_image = models.ImageField(upload_to='media/', blank=True, null=True)
    processing_date = models.CharField(max_length=50, blank=True)

    def image_preview(self):
        """ Предварительный просмотр графика """
        if self.chart_image:
            return mark_safe(f'<img src="/{self.chart_image}" width="300" height="auto" />')
        return ""


@receiver(post_save, sender=Chart)
def save_user_profile(sender, instance, created, **kwargs):
    """ Сигнал - сразу после сохранения модели, начинаем асинхронно рендерить изображение по введённым данным """
    if created:
        result = generate_image.apply_async((instance.pk, instance.chart_function,
                                            instance.chart_interval, instance.chart_step), countdown=2)
        store = result.get()
        instance.chart_image, instance.processing_date = store[0], store[1]
        instance.save()

from django.contrib import admin

from .models import Chart


class ChartAdmin(admin.ModelAdmin):
    readonly_fields = ('image_preview', 'processing_date', 'chart_image')
    list_display = ('chart_preview', 'image_preview', 'interval_preview', 'step_preview', 'date_preview')

    def chart_preview(self, obj):
        return obj.chart_function

    def image_preview(self, obj):
        return obj.image_preview()

    def interval_preview(self, obj):
        return obj.chart_interval

    def step_preview(self, obj):
        return obj.chart_step

    def date_preview(self, obj):
        return obj.processing_date

    chart_preview.short_description = 'Функция'
    image_preview.short_description = 'График'
    interval_preview.short_description = 'Интервал t, дней'
    step_preview.short_description = 'Шаг t, часы'
    date_preview.short_description = 'Дата обработки'


admin.site.register(Chart, ChartAdmin)

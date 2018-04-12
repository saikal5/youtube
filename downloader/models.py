from django.db import models


class Link(models.Model):
    url = models.URLField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.url

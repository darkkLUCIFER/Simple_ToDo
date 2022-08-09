from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=30, verbose_name='موضوع')
    body = models.TextField(verbose_name='توضیحات')
    created = models.DateTimeField(verbose_name='زمان ساخت')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'
        verbose_name = 'کار'
        verbose_name_plural = 'لیست کار ها'
        ordering = ('-created',)

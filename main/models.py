from django.db import models


class Product(models.Model):
    """ Таблица "Товары"

    - id
    - Название
    - Ссылка
    - Цена
    - Дата и время создания записи в БД
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

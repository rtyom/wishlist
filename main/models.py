from django.db import models
from django.contrib.auth.models import User


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


class WishList(models.Model):
    """ Таблица "Лист подарков"

    - id
    - Владелец
    - product
    - Видимость (bool)
    """
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)

    def __str__(self):
        return self.title

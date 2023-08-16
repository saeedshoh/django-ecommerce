from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

from authentication.models import User


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cit = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to='category', verbose_name="Картинка")

    class Meta:
        verbose_name = "Катогоия"
        verbose_name_plural = "Категории"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='ven', verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="Имя")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    contact = models.CharField(max_length=100, verbose_name="Контакты")
    chat_resp_time = models.CharField(max_length=100, verbose_name="Время для чата")
    shipping_on_time = models.CharField(max_length=100, verbose_name="Время доставки")
    authentic_rating = models.CharField(max_length=100, verbose_name="Подлинный рейтинг")
    days_return = models.CharField(max_length=100, verbose_name="Дата возврата")
    warranty_period = models.CharField(max_length=100, verbose_name="Гарантийный период")
    image = models.ImageField(upload_to=user_directory_path, verbose_name="Картинка")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


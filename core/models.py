from django.db import models
from django.urls import reverse
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from authentication.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

STATUS_CHOICE = (
    ('process', 'В процесе'),
    ('shipped', 'Отправленный'),
    ('delivered', 'Доставленный'),
)

STATUS = (
    ('draft', 'В черновике'),
    ('disabled', 'Откленен'),
    ('rejected', 'Отменен'),
    ('in_review', 'На Расмотрении'),
    ('published', 'Опубликованно'),
)

RATING = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cit = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to='category', verbose_name="Картинка", default="category.jpg")

    def get_absolute_url(self):
        return reverse('category_product_list', kwargs={'cit': self.cit})

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
    image = models.ImageField(upload_to=user_directory_path, verbose_name="Картинка", default="vendor.jpg")
    cover_image = models.ImageField(upload_to=user_directory_path, verbose_name="Изображение обложки", default="cover_product.jpg")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Tag(models.Model):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="Имя")
    description = RichTextUploadingField(null=True, blank=True, verbose_name="Описание")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория", related_name='category')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, verbose_name="Поставщик", default=None, related_name='products')
    image = models.ImageField(upload_to=user_directory_path, verbose_name="Картинка", default="cover_product.jpg")
    price = models.DecimalField(max_digits=9999999999, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(max_digits=9999999999, decimal_places=2, verbose_name='Старая цена')
    specifications = RichTextUploadingField(null=True, blank=True, verbose_name='Характеристики')
    tags = TaggableManager(verbose_name='Теги')
    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review',
                                      verbose_name='Статус продукта')

    type = models.CharField(max_length=100, verbose_name="Тип продукта", null=True, blank=True)
    life = models.DateField(verbose_name="Срок годности", null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    in_stock = models.BooleanField(default=True, verbose_name='Есть в наличии')
    featured = models.BooleanField(default=False, verbose_name='Рекомендуемый')
    digital = models.BooleanField(default=False, verbose_name='Цифровой')
    sku = ShortUUIDField(unique=True, length=4, max_length=10, verbose_name="UUID")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновление')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def get_percentage(self):
        return (self.price / self.old_price) * 100

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product-image', verbose_name='Изображения')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='images')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продуктов'


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    price = models.DecimalField(max_digits=9999999999, decimal_places=2, verbose_name='Цена')
    paid_status = models.BooleanField(default=False, verbose_name='Платный статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=10, default='process')

    class Meta:
        verbose_name = 'Корзина заказа'
        verbose_name_plural = 'Корзина заказов'


class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE, verbose_name='Заказ')
    product_status = models.CharField(max_length=200, verbose_name='Статус')
    item = models.CharField(max_length=200, verbose_name='Элемент')
    invoice_number = models.CharField(max_length=200, verbose_name='Номер счета')
    image = models.CharField(max_length=200, verbose_name='Изображения')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    price = models.DecimalField(max_digits=9999999999, decimal_places=2, verbose_name='Цена')
    total = models.DecimalField(max_digits=9999999999, decimal_places=2, verbose_name='Общий')

    class Meta:
        verbose_name = 'Товар заказа в корзине'
        verbose_name_plural = 'Товары для заказа в корзине'

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    review = models.TextField(verbose_name='Текст')
    rating = models.IntegerField(choices=RATING, default=None, verbose_name='Рейтинг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Обзор продукта'
        verbose_name_plural = 'Обзоры продуктов'

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Список желаний'
        verbose_name_plural = 'Списки желаний'

    def __str__(self):
        return self.product.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    address = models.CharField(max_length=100, null=True, verbose_name='Адрес')
    status = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

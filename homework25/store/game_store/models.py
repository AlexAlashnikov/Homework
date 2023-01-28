from django.db import models
from ckeditor.fields import RichTextField 


class ShopInfoMixin(models.Model):
    slug = models.SlugField('Индивидуальный ярлык', max_length=25, unique=True)
    description = RichTextField('Описание')
    is_active = models.BooleanField('Доступен')

    class Meta:
        abstract = True


class Category(ShopInfoMixin):
    title = models.CharField('Жанр', max_length=20)
    games_amount = models.IntegerField('Колличество игр', default=0)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='%(class)s_title_index'),
        ]

    def __str__(self):
        return f'{self.title}'


class Game(ShopInfoMixin):
    name = models.CharField('Название Игры', max_length=50)
    pub_date = models.DateField('Дата Публикации', auto_now_add=True)
    release_date = models.DateField('Дата Выхода')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    game_image = models.ImageField('Изображение Игры', upload_to='game_store/media/games')

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='%(class)s_name_index'),
            models.Index(fields=['price'], name='%(class)s_price_index'),
        ]

    def __str__(self):
        return f'{self.name}'

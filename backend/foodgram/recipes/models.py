from django.core.validators import MinValueValidator
from django.db import models


from users.models import User


class Ingredient(models.Model):

    name = models.CharField('Название ингредиента', max_length=200)
    measurement_unit = models.CharField('Единица измерения', max_length=200)

    class Meta:
        verbose_name = 'Ингредиент'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тег')
    color = models.CharField(max_length=7, verbose_name='Цвет')
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Тег'

    def __str__(self):
        return self.name


class Recipe(models.Model):

    author = models.ForeignKey(
        User,
        related_name='recipes',
        verbose_name='Автор'
    )

    name = models.CharField('Название', max_length=200)

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='recipes/'
    )

    text = models.TextField('Описание', max_length=1000)

    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тег'
    )

    cooking_time = models.IntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(1)],
        )

    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(
        verbose_name='Количество',
        validators=[MinValueValidator(1)],
    )

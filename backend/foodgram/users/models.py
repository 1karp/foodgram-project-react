from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'author')

    def __str__(self):
        return f'{self.user.username} подписался на {self.author.username}'


# class User(AbstractUser):
#     # ADMIN = 'admin'
#     # USER = 'user'
#     # ROLES = [
#     #     (ADMIN, 'Administrator'),
#     #     (USER, 'User'),
#     # ]

#     email = models.EmailField(
#         verbose_name='Адрес электронной почты',
#         max_length=254,
#         unique=True
#     )

#     username = models.CharField(
#         verbose_name='Имя пользователя',
#         max_length=150,
#         validators=[AbstractUser.username_validator],
#         unique=True
#     )
#     first_name = models.CharField(
#         verbose_name='Имя',
#         max_length=150,
#     )
#     last_name = models.CharField(
#         verbose_name='Фамилиия',
#         max_length=150,
#     )
#     role = models.CharField(
#         verbose_name='Роль',
#         max_length=50,
#         choices=ROLES,
#         default=USER
#     )

#     @property
#     def is_admin(self):
#         """Возвращает роль пользователя: Администратор
#         """
#         return self.role == self.ADMIN

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

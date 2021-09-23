from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Название группы',
                             help_text='Введите название группы')
    slug = models.SlugField(max_length=100,
                            unique=True,
                            verbose_name='Краткая ссылочка',
                            help_text='Введите краткое название ссылочки')
    description = models.TextField(max_length=200,
                                   verbose_name='Описание',
                                   help_text=('Опишите, чем примечательна'
                                              ' ваша группа'))

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              help_text=('Выберите группу,'
                                         ' в которой опубликуется пост'),
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True,
                              related_name='posts')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following')

    class Meta:
        ordering = ('-user',)
        constraints = [models.UniqueConstraint(
            fields=['user', 'following'],
            name='uniques')]

    def __str__(self):
        return f'{self.user} -> {self.following}'

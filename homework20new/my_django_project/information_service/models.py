from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    login = models.CharField(max_length=30, null=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z]{6,10}$',
            message="Логин должен начинаться с буквы и быть не больше 10 символов"
        )
    ])
    email = models.CharField(max_length=50, null=True, validators=[
        EmailValidator(
            message='Введите корректный email'
        )
    ])
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    category_id = models.IntegerField()
    category_title = models.CharField(max_length=50)

    def __str__(self):
        return f"Категория: {self.category_title}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)
    content = models.CharField(max_length=140)
    post_author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} {self.date_created} {self.content}"
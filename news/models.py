from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title_en = models.CharField(max_length=200)
    title_ta = models.CharField(max_length=200)

    content_en = models.TextField()
    content_ta = models.TextField()

    image = models.ImageField(upload_to='news/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en
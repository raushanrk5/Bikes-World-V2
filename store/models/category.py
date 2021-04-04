from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    category_slug = models.SlugField( max_length=100, unique=True, default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)
    @staticmethod

    def get_categorys():
        return Category.objects.all()
from django.db import models
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Vacancy(models.Model):
    TYPE_CHOICES = (
        ('офис', 'Офис'),
        ('дом', 'Дом'),
        ('свалка', 'Свалка'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='vacancies')
    position = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    level = models.CharField(max_length=50, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES,
                            default='офис')
    description = models.TextField(blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    city = models.CharField(max_length=100)
    requirements = models.TextField()
    experience = models.CharField(max_length=100, blank=True)
    offer = models.TextField(blank=True)
    # status = models.CharField(max_length=15, choices=STATUS_CHOICES,
                              # default='open')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'vacancies'
        ordering = ('-pk',)

    def __str__(self):
        return self.position

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.position)
        super(Vacancy, self).save(*args, **kwargs)

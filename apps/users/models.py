from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class Query(models.Model):
    text = models.CharField(max_length=255)
    text_slug = models.SlugField(max_length=255)
    last_call = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if not self.text_slug:
            self.text_slug = slugify(self.text)
        super(Query, self).save(*args, **kwargs)


class User(AbstractUser):
    queries = models.ManyToManyField(Query)

    class Meta:
        db_table = 'auth_user'

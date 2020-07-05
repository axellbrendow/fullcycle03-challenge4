from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=500)

    def __str__(self):
        return f'{{ name: "{self.name}", link: "{self.link}" }}'

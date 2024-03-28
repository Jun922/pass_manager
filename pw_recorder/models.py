from django.db import models


class App(models.Model):
    name = models.CharField(null=False, max_length=20)
    password = models.CharField(unique=True, null=False, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
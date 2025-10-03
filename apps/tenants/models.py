from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    domain = models.CharField(
        max_length=255, unique=True, null=True
    )  # Add domain as nullable

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"

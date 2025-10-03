from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __str__(self):
        return self.name

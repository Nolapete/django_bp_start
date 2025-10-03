from django.db import models


class Product(models.Model):
    tenant = models.ForeignKey(
        "tenants.Tenant", on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Use the string-based reference for the user model
    created_by = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __str__(self):
        return self.name

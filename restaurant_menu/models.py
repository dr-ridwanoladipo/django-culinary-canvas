from django.db import models
from django.contrib.auth.models import User

# Choices for meal types and item status
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Item(models.Model):
    """
    Represents a menu item in the restaurant.
    """
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # PROTECT/SET_NULL
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal


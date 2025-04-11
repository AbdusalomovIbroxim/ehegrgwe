from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                   help_text="Enter discount as percentage")
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.FloatField(default=0.0)
    review_count = models.PositiveIntegerField(default=0)
    favorites = models.ManyToManyField(User, related_name='favorite_products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True,
                                    blank=True)

    def save(self, *args, **kwargs):
        if self.discount:
            self.discounted_price = self.price - (self.price * (self.discount / 100))
        else:
            self.discounted_price = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta(days=10))

    def get_time_remaining(self):
        end_date = self.start_date + self.duration
        remaining_time = end_date - timezone.now()

        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

from django.db import models

class Order(models.Model):
    sender_name = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    package_details = models.TextField()
    delivery_preferences = models.TextField()
    status = models.CharField(max_length=50, default='Processing')

    def __str__(self):
        return f"Order {self.id}"

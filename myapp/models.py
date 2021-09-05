from django.db import models
from django.utils import timezone
# Create your models here.
STATUS_CHOICES = (
    ('pending','PENDING'),
    ('bought', 'BOUGHT'),
    ('not available','NOT AVAILABLE'),
)
class GroceryUpload(models.Model):
    itemname = models.CharField(max_length=50, blank=True, null=True)
    itemquantity = models.IntegerField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(null=True, blank=True,default=timezone.localtime(timezone.now()))
    uploadedby = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.itemname
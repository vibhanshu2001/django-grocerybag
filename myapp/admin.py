from django.contrib import admin
from .models import GroceryUpload
# Register your models here.
class GroceryUploadAdmin(admin.ModelAdmin):
    list_display = ('itemname','itemquantity','status','date','uploadedby')
admin.site.register(GroceryUpload,GroceryUploadAdmin)
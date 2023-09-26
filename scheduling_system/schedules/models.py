from datetime import timezone
from django.db import models

from authentication.models import AppUser

# Create your models here.

class Technical(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    technical = models.ForeignKey(Technical, on_delete=models.CASCADE)
    description = models.TextField(max_length=750, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title
    
class Changes(models.Model):
    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="owner")
    edited_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="edited_by")

    # old items
    old_title = models.CharField(max_length=100)
    old_address = models.CharField(max_length=200)
    old_technical = models.ForeignKey(Technical, on_delete=models.CASCADE, related_name="old_technical")
    old_description = models.TextField(max_length=750, blank=True)
    old_date = models.DateField()
    old_start_time = models.TimeField()
    old_end_time = models.TimeField()

    # new items
    new_title = models.CharField(max_length=100)
    new_address = models.CharField(max_length=200)
    new_technical = models.ForeignKey(Technical, on_delete=models.CASCADE, related_name="new_technical")
    new_description = models.TextField(max_length=750, blank=True)
    new_date = models.DateField()
    new_start_time = models.TimeField()
    new_end_time = models.TimeField()


    def __str__(self):
        return self.new_title
    
class Deleted_Event(models.Model):
    created = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="deleted_owner")
    deleted_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="deleted_by")
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    technical = models.ForeignKey(Technical, on_delete=models.CASCADE, related_name="deleted_technical")
    description = models.TextField(max_length=750, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title


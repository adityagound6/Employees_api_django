from django.db import models

# Create your models here.
class Employee(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    note_text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
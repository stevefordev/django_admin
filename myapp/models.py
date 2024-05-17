# myapp/models.py
from django.db import models

class Alert(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    received_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

#python manage.py makemigrations
#python manage.py migrate

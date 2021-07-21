from django.db import models
from datetime import datetime

# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=255)
    uploadDateTime = models.DateTimeField(default=datetime.now())
    image = models.ImageField(upload_to='images/', )
    def __str__(self):
        return str(self.id) + ' ' + self.title
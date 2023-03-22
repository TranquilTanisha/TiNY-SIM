from django.db import models
import uuid
# Create your models here.

class Encode(models.Model):
    image = models.ImageField(upload_to='encoded/', default='images/test2.png')
    filename=models.CharField(max_length=100)
    message = models.TextField()
    key=models.CharField(max_length=10, default=None)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.message
    
class Decode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')
    message = models.TextField()
    key=models.CharField(max_length=10, default="")

    def __str__(self):
        return self.message
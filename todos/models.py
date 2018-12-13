from django.db import models
from datetime import datetime
# Create your models here.


class Todo(models.Model):

    title=models.CharField(max_length=200,null=False)
    text=models.TextField(null=False)
    created_at=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title

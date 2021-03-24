from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    data = models.DateField(auto_now=True, null=True)
    foto = models.ImageField(upload_to="todo/",null=True)

    def __str__(self):
        return self.title




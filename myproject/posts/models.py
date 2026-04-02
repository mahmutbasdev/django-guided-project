from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body  = models.TextField(default="")                    
    slug  = models.SlugField(default="")
    date  = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f" {self.title} -  {self.slug} - {self.date}"
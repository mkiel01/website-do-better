from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self): #print(my_task)/ str(my_task) zwróci w tym wypadku self.title 
        return self.title

    # class Meta:
    #     ordering = ['complete']
    class Meta: #dodatkowe właściwosć (nie dodają pól do bazy danych)
       order_with_respect_to = 'user'
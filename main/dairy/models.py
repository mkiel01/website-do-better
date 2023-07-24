from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

class dairy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    text = models.TextField(max_length=200, default='write something my boi')
    date_posted = models.DateTimeField(auto_now_add=True)

    RED = 'R'
    BLUE = 'B'
    GREEN = 'G'
    DEFAULT = 'D'


    COLOR_TYPE_CHOICES = [
        (RED, 'RED'),
        (BLUE,'BLUE'),
        (GREEN,'Green'),
        (DEFAULT, 'default'),
    ]

    color_type = models.CharField(max_length=1, choices=COLOR_TYPE_CHOICES, default=DEFAULT)
    

# add instant date created wgen dairy is added and then primaty key to add realtionship parent-child and then 
#on_delete=models.CASCADE
#imprment order by method as well
# add .filter() method as well

#blank
#If True, the field is allowed to be blank. Default is False.

#Metadata is an optional entity within a model and it is anything that is not a field.
    def __str__(self):

        return self.text
    
    #now on my website it is ordering with rest to color_type fild in database by alphabetical order
    class Meta:
        ordering = ["color_type"]
    

# if you want to interact with the database with the model, for example create an instance of the model and save it or retrieve the model from db,

# def __str__(self):
#     return self.name 
  
    
    




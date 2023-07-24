from django.db import models


# Create your models here.

class hours(models.Model):
    
    inputhour = models.IntegerField()
    hourtomin = models.IntegerField(blank=True, null=True)
    

    def __str__(self):

        return str(self.inputhour)
    
    def save(self, *args, **kwargs):
        self.hourtomin = self.inputhour * 60
        super(hours, self).save(*args, **kwargs)

    

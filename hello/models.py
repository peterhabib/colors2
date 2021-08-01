from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)



class Data(models.Model):
    Name= models.CharField(max_length=100)
    Age= models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Adress= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Name} - {self.Age} - {self.Email} - {self.Adress}'

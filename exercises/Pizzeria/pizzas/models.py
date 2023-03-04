from django.db import models

# Create your models here.


class Pizza(models.Model):
    '''A type of pizza sold at the Pizzeria'''
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        '''Return a string representation of the model '''
        return self.name


class Topping(models.Model):
    '''Topping on a pizza'''
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self) -> str:
        '''Return a string representation of the model '''
        return self.name

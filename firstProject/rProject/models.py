from django.db import models
# from 
# Create your models here.
class chaiModel(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ma','mango chai'),
        ('um', 'umesh chai')
        ('cm', 'chai master')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    date = models.DateTimeField(default=timeZone)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
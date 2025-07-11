from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class chaiModel(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ma','mango chai'),
        ('um', 'umesh chai'),
        ('cm', 'chai master')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE,default='ML')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    
# one two many model


class ChaiReviews(models.Model):
    CHAI_RATING =[
        ('1',1),('2',2),('3',3),('4',4),('5',5)
    ]
    chai = models.ForeignKey(chaiModel, on_delete=models.CASCADE, related_name='chaiReviews' )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userName' )
    rating = models.IntegerField(max_length=5, choices=CHAI_RATING,default=1)
    comment = models.TextField()
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.userName} review for {self.chai.name}'
    
# many to many relation

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(chaiModel, related_name='stores')


    def __str__(self):
        return self.name
    
# one to one relation

class chaiCertificate(models.Model):
    chai= models.OneToOneField(chaiModel, on_delete=models.CASCADE, related_name='certificate')
    number = models.CharField(max_length=10)
    issuseFeild = models.DateTimeField(default=timezone.now)
    vaild_until = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.chai.name}'




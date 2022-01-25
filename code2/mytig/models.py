from django.db import models

# Create your models here.
class ProduitEnPromotion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)

class ProduitIsAvaible(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)

class ProduitStock(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')
    inStock = models.IntegerField(default='-1')
    sale = models.BooleanField(default=False)
    discount = models.FloatField(default='0.0')

    class Meta:
        ordering = ('tigID',)

class ProduitInSale(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')

    class Meta:
        ordering = ('tigID',)

class ProduitTransaction(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default=-1)
    transactionPrice = models.FloatField(default=0.0)
    quantite = models.IntegerField(default=-1)
    type = models.CharField(default="mer",max_length=20)

    class Meta:
        ordering = ('tigID',)

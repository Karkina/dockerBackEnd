from django.core.management.base import BaseCommand, CommandError
from mytig.models import ProduitStock
from mytig.serializers import ProduitStockSerializer
from mytig.config import baseUrl
import requests
import time

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        ProduitStock.objects.all().delete()
        for product in jsondata:
            if product['sale']:
                serializer = ProduitStockSerializer(data={'tigID':str(product['id']),'inStock':int(2),'sale':product['sale'],'discount':product['discount']})
            else:
                serializer = ProduitStockSerializer(data={'tigID': str(product['id']), 'inStock': int(2)})
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')


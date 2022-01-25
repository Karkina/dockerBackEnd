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
        for object in ProduitStock.objects.all():
            serializer = ProduitStockSerializer(object)
            print( serializer.data['inStock'], serializer.data['tigID'],serializer.data['sale'],serializer.data['discount'])

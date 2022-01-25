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
            serializer = ProduitStock(object)
            if (serializer.data['tigID'] == 12):
                ProduitStockSerializer.objects.filter(tigID=12).delete()
                val = serializer.data['inStock'] + 2
                serializer = ProduitStockSerializer(data={'tigID': str(12), 'inStock': val})
                if serializer.is_valid():
                    serializer.save()
            print( serializer.data['inStock'], serializer.data['tigID'])

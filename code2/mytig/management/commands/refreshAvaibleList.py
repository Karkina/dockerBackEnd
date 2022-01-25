from django.core.management.base import BaseCommand
from mytig.models import ProduitIsAvaible
from mytig.serializers import ProduitAvaibleSerializer
from mytig.config import baseUrl
import requests
import time

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        ProduitIsAvaible.objects.all().delete()
        for product in jsondata:
            if product['availability']:
                serializer = ProduitAvaibleSerializer(data={'tigID':str(product['id'])})
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')


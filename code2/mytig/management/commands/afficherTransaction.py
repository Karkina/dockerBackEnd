from django.core.management.base import BaseCommand, CommandError
from mytig.models import ProduitTransaction
from mytig.serializers import ProduitTransactionSerializer
from mytig.config import baseUrl
import requests
import time

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        for object in ProduitTransaction.objects.all():
            serializer = ProduitTransactionSerializer(object)
            print( serializer.data['created'], serializer.data['tigID'],serializer.data['quantite'],serializer.data['transactionPrice'])

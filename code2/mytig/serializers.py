from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion, ProduitIsAvaible,ProduitStock,ProduitTransaction

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')

class ProduitAvaibleSerializer(ModelSerializer):
    class Meta:
        model = ProduitIsAvaible
        fields = ('id', 'tigID')

class ProduitStockSerializer(ModelSerializer):
    class Meta:
        model = ProduitStock
        fields = ('tigID','inStock','sale','discount')

class ProduitTransactionSerializer(ModelSerializer):
    class Meta:
        model = ProduitTransaction
        fields = ('created','type','tigID','quantite','transactionPrice')
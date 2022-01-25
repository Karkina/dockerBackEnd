import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from mytig.config import baseUrl
from rest_framework.exceptions import NotFound
from mytig.models import ProduitStock,ProduitTransaction
from mytig.serializers import ProduitStockSerializer,ProduitTransactionSerializer,ProduitTransactionSerializer
# Create your views here.

class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        res = []
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if(serializer.data['tigID'] == pk):
                    val = serializer.data['inStock']
                    sale = serializer.data['sale']
                    discount = serializer.data['discount']
                    break
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            jsondata['inStock']=val
            jsondata['sale'] = sale
            jsondata['discount'] = discount
            return Response(jsondata)
        except:
            raise Http404

class RedirectionTransaction(APIView):
    def get(self,request,format = None):
        try:
            res = []
            for prod in ProduitTransaction.objects.all():
                serializer = ProduitTransactionSerializer(prod)
                jsondata = dict()
                jsondata["pk"] = serializer.data["tigID"]
                jsondata["price"] = serializer.data["transactionPrice"]
                jsondata["quantite"] = serializer.data["quantite"]
                jsondata["type"] =serializer.data["type"]
                jsondata["date"] = serializer.data["created"]

                res.append(jsondata)
            return JsonResponse(res, safe=False)
        except:
            raise Http404

class RedirectionIncrementStock(APIView):
    def get(self, request, pk,number, prix,format=None):
        res = []
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if(serializer.data['tigID'] == pk):

                    val = serializer.data['inStock'] + number
                    response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                    jsondata = response.json()
                    if(jsondata['category']==0) : typeSerialize = "poissons"
                    if (jsondata['category'] == 1): typeSerialize = "Fruit de mer"
                    if (jsondata['category'] == 2): typeSerialize = "Crustace"

                    serializerPrix = ProduitTransactionSerializer(data={'tigID':str(pk),'type':
                                                            typeSerialize,'transactionPrice':-prix,'quantite':number})
                    serializer = ProduitStockSerializer(data={'tigID': str(pk), 'inStock': val})
                    if serializer.is_valid():
                        ProduitStock.objects.filter(tigID=pk).delete()
                        serializer.save()
                    if serializerPrix.is_valid():
                        serializerPrix.save()
                    break

            response = requests.get(baseUrl + 'product/' + str(pk) + '/')
            jsondata = response.json()
            jsondata['inStock'] = val
            return Response(jsondata)
        except:
            raise Http404

class RedirectionDecrementStock(APIView):
    def get(self, request, pk,number,prix, format=None):
        res = []
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if(serializer.data['tigID'] == pk):
                    val = int(serializer.data['inStock'] - number)
                    if(val <=0):
                        raise NotFound('Plus de stock')
                    else:
                        response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                        jsondata = response.json()
                        if (jsondata['category'] == 0): typeSerialize = "poissons"
                        if (jsondata['category'] == 1): typeSerialize = "FruitDeMer"
                        if (jsondata['category'] == 2): typeSerialize = "Crustace"
                        serializerPrix = ProduitTransactionSerializer(data={'tigID': str(pk),'type':typeSerialize, 'transactionPrice': prix, 'quantite': number})
                        serializer = ProduitStockSerializer(data={'tigID': str(pk), 'inStock': val})
                        if serializer.is_valid():
                            ProduitStock.objects.filter(tigID=pk).delete()
                            serializer.save()

                        if serializerPrix.is_valid():
                            serializerPrix.save()
                    break

            response = requests.get(baseUrl + 'product/' + str(pk) + '/')
            jsondata = response.json()
            jsondata['inStock'] = val
            return Response(jsondata)
        except:
            raise Http404

class PutOnsale(APIView):
    def get(self, request, pk, newprice, format=None):
        try:
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                if (serializer.data['tigID'] == pk):
                    if(newprice <0):
                        raise Http404
                    else:
                        ProduitStock.objects.filter(tigID=pk).delete()
                        serializer = ProduitStockSerializer(data={'tigID': str(pk), 'inStock': serializer.data['inStock'],'sale':True,'discount':newprice})
                        if serializer.is_valid():
                            serializer.save()
                    break
            return HttpResponse(status=200)
        except:
            raise Http404


class RedirectionPoissons(APIView):
    def get(self, request, format=None):
        try:
            res = []
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                jsondata = response.json()
                if jsondata['category']==0:
                    jsondata['inStock']=serializer.data['inStock']
                    jsondata['sale'] = serializer.data['sale']
                    jsondata['discount'] = serializer.data['discount']
                    res.append(jsondata)
                else:
                    pass
            return  JsonResponse(res, safe=False)
        except:
            raise Http404

class RedirectionCrustaces(APIView):
    def get(self, request, format=None):
        try:
            res = []
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                jsondata = response.json()
                if jsondata['category']==2:
                    jsondata['inStock']=serializer.data['inStock']
                    jsondata['sale'] = serializer.data['sale']
                    jsondata['discount'] = serializer.data['discount']
                    res.append(jsondata)
                else:
                    pass
            return  JsonResponse(res, safe=False)
        except:
            raise Http404

class RedirectionFruitDeMer(APIView):
    def get(self, request, format=None):
        try:
            res = []
            for prod in ProduitStock.objects.all():
                serializer = ProduitStockSerializer(prod)
                response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
                jsondata = response.json()
                if jsondata['category']==1:
                    jsondata['inStock']=serializer.data['inStock']
                    jsondata['sale'] = serializer.data['sale']
                    jsondata['discount'] = serializer.data['discount']
                    res.append(jsondata)
                else:
                    pass
            return  JsonResponse(res, safe=False)
        except:
            raise Http404


from mytig.models import ProduitEnPromotion,ProduitIsAvaible
from mytig.serializers import ProduitEnPromotionSerializer,ProduitAvaibleSerializer
from django.http import Http404
from django.http import JsonResponse

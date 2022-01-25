from django.urls import path,register_converter
from mytig import views,converts


register_converter(converts.FloatUrlParameterConverter, 'float')
urlpatterns = [
    path('infoproducts/', views.RedirectionListeDeProduits.as_view()),
    path('infoproduct/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('putonsale/<int:pk>/<int:newprice>/', views.PutOnsale.as_view()),
    path('infopoissons/',views.RedirectionPoissons.as_view()),
    path('infocrustaces/',views.RedirectionCrustaces.as_view()),
    path('infofruitdemers/',views.RedirectionFruitDeMer.as_view()),
    path('incrementStock/<int:pk>/<int:number>/<float:prix>',views.RedirectionIncrementStock.as_view()),
    path('decrementStock/<int:pk>/<int:number>/<float:prix>', views.RedirectionDecrementStock.as_view()),
    path('transaction/',views.RedirectionTransaction.as_view()),
]

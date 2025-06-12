from django.urls import path
from .views import log,reg,bootstrap,index,product_table,demo

urlpatterns=[
    path('log/',log),
    path('reg/',reg),
    path('bootstrap/',bootstrap),
    path('index/',index),
    path('product_table/',product_table),
    path('demo-function/',demo),
]
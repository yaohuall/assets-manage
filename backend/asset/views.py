from asset.models import Assets
from asset.serializers import AssetsSerialzer
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
import akshare as ak
import pandas as pd
import datetime
import requests
import json

# Create your views here.
# class exchangeRate(APIView):
#     ################ https://openapi.taifex.com.tw/v1/DailyForeignExchangeRates #################
#     """ This view make and external api call, save the result and return 
#     the data generated as json object """
#     def get(self, request):
#         # Make an external api request ( use auth if authentication is required for the external API)
#         r = requests.get('https://openapi.taifex.com.tw/v1/DailyForeignExchangeRates')
#         r_status = r.status_code
#         response = []

#         if r_status == 200:
#             data = r.json()[0]
#             # print(data)
#             usd_rate = data['USD/NTD']
#             cny_rate = data['RMB/NTD']
#             response.append({'CURRENCY':'1 USD', 'RATE':usd_rate})
#             response.append({'CURRENCY':'1 CNY', 'RATE':cny_rate})
#             response_json = json.dumps(response)
#         else:
#             return Response({'message':'Internet error!'}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(response)

# class rateChart(APIView):
#     def get(self, request):
#         today = datetime.date.today().strftime("%Y%m%d")
#         start_day = (datetime.date.today() - datetime.timedelta(days=180)).strftime("%Y%m%d")
#         currency_hist_df = ak.currency_hist(symbol="usd-twd", start_date=start_day, end_date=today)
#         usd = currency_hist_df['收盘'].values
#         series = pd.date_range(start=start_day, end=today, freq='D')
#         period = series.strftime("%Y%m%d").to_list()

#         return Response({'time':period, 'data':usd})

class AssetsViewSet(ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerialzer
    # permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    # to let backend which creator is assigned to
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)




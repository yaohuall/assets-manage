from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import finnhub
from rest_framework.response import Response

# Create your views here.
class stockList(APIView):
        def get(self, request):
            # today = datetime.date.today().strftime("%Y%m%d")
            # start_day = (datetime.date.today() - datetime.timedelta(days=180)).strftime("%Y%m%d")
            # currency_hist_df = ak.currency_hist(symbol="usd-twd", start_date=start_day, end_date=today)
            # usd = currency_hist_df['收盘'].values
            # series = pd.date_range(start=start_day, end=today, freq='D')
            # period = series.strftime("%Y%m%d").to_list()

            finnhub_client = finnhub.Client(api_key="cbk9p2qad3if4577vqgg")

            current_price = finnhub_client.quote('NVDA')['c']
            return Response({'data': current_price})
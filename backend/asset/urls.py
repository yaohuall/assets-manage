# ============== 导入模块 ===============
from django.urls import path
from rest_framework.routers import DefaultRouter
from asset import views
from asset.views import AssetsViewSet

app_name = 'asset'
router = DefaultRouter()


router.register('assets', AssetsViewSet, basename='assets')  # http://127.0.0.1:8000/api/v1/assets/

urlpatterns = [
    # path('rates/', views.exchangeRate.as_view(), name='rates'),
    # path('rate-chart/', views.rateChart.as_view(), name='rate-chart'),
]


urlpatterns += router.urls
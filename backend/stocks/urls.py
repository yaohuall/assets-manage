# ============== 导入模块 ===============
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
# from asset.views import AssetsViewSet

app_name = 'stocks'
router = DefaultRouter()


# router.register('stocks', AssetsViewSet, basename='stocks')  # http://127.0.0.1:8000/api/v1/assets/

urlpatterns = [
        path('stocks/', views.stockList.as_view(), name='stocks'),
]


urlpatterns += router.urls
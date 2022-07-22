from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Assets(models.Model):
    STOCK = 'stock'
    SALARY = 'salary'
    PAY = 'pay'
    RECEIVED = 'received'
    SPEND = 'spend'

    ASSET_TYPES = (
        (STOCK, 'Stock'),
        (SALARY, 'Salary'),
        (PAY, 'Pay'),
        (RECEIVED, 'Received'),
        (SPEND, 'Spend'),
    )

    name = models.CharField(max_length=255, blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    purchased_price = models.IntegerField(blank=True, null=True)
    actual_price = models.IntegerField(blank=True, null=True)
    asset_type = models.CharField(max_length=255, choices=ASSET_TYPES, default=SPEND)
    date = models.DateField(blank=True, null=True)
    # 在 SET_NULL 的情況下，顧名思義，當刪除一個引用物件時，所有引用物件的引用物件都設定為 NULL。這種關係要求引用的物件欄位可以為空。 返回id值
    # assigned_to = models.ForeignKey(User, related_name='assignedleads', blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, related_name='assets', on_delete=models.CASCADE)

    # auto_now_add:第一次創建時更新時間
    created_at = models.DateField(auto_now_add=True)
    # auto_now：每次修改更新時間
    modified_at = models.DateField(auto_now=True)
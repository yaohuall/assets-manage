# ============== 导入模块 ===============
from rest_framework import serializers
from asset.models import Assets

class AssetsSerialzer(serializers.ModelSerializer):
    # created_by = 
    class Meta:
        model = Assets
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at'
        )
        fields = (
            'id',
            'name', 
            'memo', 
            'purchased_price', 
            'actual_price', 
            'asset_type',
            'date', 
        )
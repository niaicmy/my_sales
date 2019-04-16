from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(GoodsInfo)
# admin.site.register(SaleRecords)identifier.sqlite


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    # list_display设置要显示在列表中的字段
    list_display = ('commodityCode', 'commodityName', 'commodityWarning', 'commodityTotal', 'commodityCost',
                    'commodityTotalPrice', 'commodityProfit', 'commodityTime')
    pass


@admin.register(SaleRecords)
class SaleRecordsAdmin(admin.ModelAdmin):
    list_display = ('saleCode', 'commodityCode', 'commodityName', 'saleNum', 'saleUnitPrice', 'saleDiscount',
                    'saleTotalPrice', 'saleDateTime', 'saleSuccess')
    # list_display = ('saleCode', 'SaleDetails', 'saleDateTime', 'saleSuccess')
    pass

from django.apps import AppConfig


class SalesRecondsConfig(AppConfig):
    name = 'sale_records'

    # 更改 APP 在admin后台显示的命名
    verbose_name = '商品销售汇总'
    verbose_name_plural = '商品销售汇总'

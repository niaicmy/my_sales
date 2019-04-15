from django.db import models

# Create your models here.
# 注意：Django 1.7 及以上的版本需要连续执行以下命令
# python manage.py makemigrations
# python manage.py migrate


# GoodsInfo 货物总类检索
class GoodsInfo(models.Model):
    """
    商品目录列表类 包含: 商品编码 商品名称 商品预警值 商品销售总数量 商品销售总成本金额 商品销售总金额 商品总利润 商品数据更新日期
    """
    # 商品编码 B00001 T00001
    commodityCode = models.CharField(max_length=8, primary_key=True, verbose_name='商品编码')
    commodityName = models.CharField(max_length=20, verbose_name='商品名称')

    # 库存预警
    commodityWarning = models.PositiveIntegerField(default=2, verbose_name='商品预警值')
    # 商品销售总数量
    commodityTotal = models.PositiveIntegerField(default=0, verbose_name='商品销售总数')
    # 商品销售总成本
    commodityCost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总成本')
    # 商品销售总金额
    commodityTotalPrice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总金额')
    # 商品总利润
    commodityProfit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总利润')
    # 最后统计时间
    commodityTime = models.DateField(auto_now_add=True, verbose_name='统计日期')

    # 定义元选项
    class Meta:
        db_table = 'GoodsInfo'  # 指定生成的数据表名为GoodsInfo
        verbose_name = '商品销售汇总'
        verbose_name_plural = '商品销售汇总'
        ordering = ['commodityCode']


# SaleRecords 每日每单销售记录 行为单位
class SaleRecords(models.Model):
    """
    商品销售类 包含： 商品编码 商品名称 销售数量 销售单价 销售折扣 销售总金额 销售时间 是否成交
    """
    # 销售唯一序号0x0001
    saleCode = models.CharField(max_length=10, verbose_name='订单序号')
    # 商品编码 B00001 T00001
    commodityCode = models.CharField(max_length=8, verbose_name='商品编码')
    commodityName = models.CharField(max_length=20, verbose_name='商品名称')

    # 单个品种单次销售数量
    saleNum = models.PositiveSmallIntegerField(default=1, verbose_name='商品数量')
    # 单价
    saleUnitPrice = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='商品单价')
    # 折扣
    saleDiscount = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='商品折扣')
    # 成交总金额
    saleTotalPrice = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='商品总金额')

    saleDateTime = models.TimeField(auto_now_add=True, verbose_name='销售时间')
    saleSuccess = models.BooleanField(default=False, verbose_name='是否成功')

    # 定义元选项
    class Meta:
        db_table = 'SalesRecords'  # 指定生成的数据表名为SalesRecords
        verbose_name = '销售记录'
        verbose_name_plural = '销售记录'
        ordering = ['saleCode']


# 销售日表 周表 月表 季表 年表 需要吗？ 还是python查询计算？
# SaleRecordsDay 每日销售记录
# class SaleRecordsDay(models.Model):
#     """
#     商品销售类 包含： 商品编码 商品名称 每日销售数量 每日总金额 日销售时间
#     """
#     # 序号
#     allNum = models.AutoField()
#     # 商品编码 B00001 T00001
#     commodityCode = models.CharField(max_length=8, primary_key=True)
#     commodityName = models.CharField(max_length=20, primary_key=True)
#     saleNum = models.PositiveSmallIntegerField(default=1)
#     saleUnitPrice = models.DecimalField(max_digits=6, decimal_places=2)
#     saleTotalPrice = models.DecimalField(max_digits=7, decimal_places=2)
#     saleDateTime = models.DateField(auto_now_add=True)
#
#     # 定义元选项
#     class Meta:
#         db_table = 'SalesRecordsDay'  # 指定生成的数据表名为SalesRecordsDay
#     pass

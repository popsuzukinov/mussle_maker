from django.db import models


# Create your models here.
class Musslemenu(models.Model):
    workout_datetime = models.DateTimeField('筋トレ日時', blank=True, null=True)
    where_wana_make_body = models.CharField('鍛える部位', max_length=20, blank=True, null=True)
    remarks = models.CharField('備考', max_length=50, blank=True, null=True)


class Detailmusslemenu(models.Model):
    Musslemenu = models.ForeignKey(Musslemenu, on_delete=models.CASCADE)
    menu1 = models.CharField('メニュー1', max_length=20, blank=True, null=True)
    menu2 = models.CharField('メニュー2', max_length=20, blank=True, null=True)
    menu3 = models.CharField('メニュー3', max_length=20, blank=True, null=True)
    menu4 = models.CharField('メニュー4', max_length=20, blank=True, null=True)
    menu5 = models.CharField('メニュー5', max_length=20, blank=True, null=True)
    menu6 = models.CharField('メニュー6', max_length=20, blank=True, null=True)
    menu7 = models.CharField('メニュー7', max_length=20, blank=True, null=True)
    menu8 = models.CharField('メニュー8', max_length=20, blank=True, null=True)
    menu9 = models.CharField('メニュー9', max_length=20, blank=True, null=True)


from django.db import models


# Create your models here.
class Musslemenu(models.Model):
    workout_datetime = models.DateTimeField('筋トレ日時', blank=True, null=True)
    where_wana_make_body = models.CharField('鍛える部位', max_length=20, blank=True, null=True)
    big3 = models.CharField('ビッグ3', max_length=20)
    remarks = models.CharField('備考', max_length=50, blank=True, null=True)


class Detailmusslemenu(models.Model):
    Musslemenu = models.ForeignKey(Musslemenu, on_delete=models.CASCADE)
    menu1 = models.CharField('メニュー1', max_length=20, blank=True, null=True)

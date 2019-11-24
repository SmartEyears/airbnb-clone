from django.db import models


class TimeStampModel(models.Model):

    """ TimeStampModel """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 모델이 데이터베이스에 등록되지 않도록 adstrct
    class Meta:
        abstract = True

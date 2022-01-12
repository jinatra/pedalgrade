from django.db import models

from core.models import TimeStampModel, SoftDeleteModel

# 페달 그레이드 구독 유저
class GradeUser(TimeStampModel, SoftDeleteModel):
    email = models.CharField(max_length=512, unique=True)

    class Meta:
        db_table = 'grade_users'


# 페달 구독 유저
class PedalUser(TimeStampModel, SoftDeleteModel):
    email = models.CharField(max_length=512, unique=True)

    class Meta:
        db_table = 'pedal_users'

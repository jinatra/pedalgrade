from django.db import models

from core.models import TimeStampModel, SoftDeleteModel

class Board(TimeStampModel, SoftDeleteModel):
    title   = models.CharField(max_length=128)
    content = models.TextField()
    type    = models.CharField(max_length=64)

    class Meta:
        db_table = 'boards'

class Image(TimeStampModel, SoftDeleteModel):
    img_url = models.CharField(max_length=2048)

    class Meta:
        db_table = 'images'

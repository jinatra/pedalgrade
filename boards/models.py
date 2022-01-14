from django.db import models

from core.models import TimeStampModel, SoftDeleteModel

class Board(TimeStampModel, SoftDeleteModel):
    title   = models.CharField(max_length=256)
    content = models.TextField()
    type    = models.CharField(max_length=64)

    class Meta:
        db_table = 'boards'

class Image(TimeStampModel, SoftDeleteModel):
    img_url = models.CharField(max_length=2048)
    type    = models.CharField(max_length=64)
    board   = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'
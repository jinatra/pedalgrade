from django.db import models

from core.models import TimeStampModel, SoftDeleteModel

class GradeUser(TimeStampModel, SoftDeleteModel):
    email = models.CharField(max_length=512, unique=True)

    class Meta:
        db_table = 'grade_users'

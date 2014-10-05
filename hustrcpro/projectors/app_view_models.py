from django.db import models
from projectors.models import *

class Projectorstatus(models.Model):
    #projector = models.ForeignKey(Projector, blank=True, null=True)
    projector_id = models.IntegerField(blank=True, null=True)
    s_r_id = models.IntegerField(primary_key=True)
    status_id = models.IntegerField(blank=True, null=True)
    status_name = models.CharField(max_length=45, blank=True)
    date_register = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'view_projector_status'

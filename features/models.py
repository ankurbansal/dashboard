from django.db import models
from core.models import Build, Device

# Create your models here.
class Features(models.Model):
    feature_id= models.AutoField(primary_key=True);
    featureName=models.CharField(max_length=100,null=True);
    outcome=models.NullBooleanField();
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
    def primary_key(self):
        return self.feature_id
    def __unicode__(self):
        return self.featureName

class FeatureResult(models.Model):
    result_id= models.AutoField(primary_key=True);
    outcome_result=models.BooleanField();
    feature=models.ForeignKey(Features);
    feature_name= models.CharField(max_length="20");
    build = models.ForeignKey(Build);
    device = models.ForeignKey(Device)
    device_info=models.CharField(max_length='20')
    build_number=models.CharField(max_length="20");
    render_mode=models.CharField(max_length="20");
    release_number=models.CharField(max_length="30");
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
    # many to many relationship to devices with assoc table
from django.db import models
from core.models import Build, Device

class RealWorldApp(models.Model):
    realworldapp_id= models.AutoField(primary_key=True);
    realworldapp_name= models.TextField(max_length=400);
    outcome=models.NullBooleanField();
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
    def primary_key(self):
        return self.realworldapp_id
    def __unicode__(self):
        return self.realworldapp_name
    
class RealWorldAppResult(models.Model):
    result_id= models.AutoField(primary_key=True);
    outcome_result=models.BooleanField();
    realworldapp=models.ForeignKey(RealWorldApp);
    realworldapp_name= models.CharField(max_length="30");
    build = models.ForeignKey(Build,);
    build_number=models.CharField(max_length="20");
    device = models.ForeignKey(Device)
    device_info=models.CharField(max_length='20')
    render_mode=models.CharField(max_length="20");
    target=models.CharField(max_length="20");
    release_number=models.CharField(max_length="30");
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
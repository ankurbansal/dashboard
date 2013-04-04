from django.db import models
from random import choice
from test.test_imageop import MAX_LEN

# Create your models here.
class TestCase(models.Model):
#    test_id= models.AutoField(primary_key=True);
#   test_name= models.TextField(max_length=400);
    test_path= models.TextField(max_length=100,null=True);
    test_area= models.CharField(max_length=100,null=True);
    suite=models.CharField(max_length=100,null=True);
    swfName=models.CharField(max_length=100,null=True);
#    outcome=models.NullBooleanField();
#    mainArea=models.CharField(max_length=100,null=True);
#    isAir = models.NullBooleanField(default=False);
#    section_id= models.CharField(max_length=100);

#    last_pass=models.DateField();
#    last_fail=models.DateField();
    outcome=models.NullBooleanField();
    test_caseid = models.IntegerField(primary_key=True);
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
    def primary_key(self):
        return self.test_caseid
    def __unicode__(self):
        return self.swfName
    
#    class Meta:
#        db_table="data_testcase"
##        exclude = ['outcome']
        
        

class Device(models.Model):
    device_id= models.AutoField(primary_key=True);
    device_type=(
        (u'IPhone',u'iPhone'),
        (u'IPOD',u'iPod'),
        (u'IPAD',u'iPad'),
        (u'Phone',u'Phone'),
        (u'Pad',u'Pad')
    )
    name=models.CharField(max_length=20);
    device_type=models.CharField(max_length=20,choices=device_type);
    OS_type=models.CharField(max_length=20);
    OS_version=models.CharField(max_length=10);
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
    def __unicode__(self):
        return (str(self.name) +"|"+ str(self.OS_type) +"|" + str(self.OS_version))
    
class Build(models.Model):
    build_id= models.AutoField(primary_key=True);
    number=models.CharField(max_length=20);
    product_version=models.CharField(max_length=20);
    branch_name=models.CharField(max_length=20);
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
    def __unicode__(self):
        return (str(self.number) +"|"+ str(self.product_version) )
    
    
    
   
class Result(models.Model):
    result_id= models.AutoField(primary_key=True);
    outcome_result=models.BooleanField();
    test_case=models.ForeignKey(TestCase);
    test_case_name= models.CharField(max_length="20");
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
        



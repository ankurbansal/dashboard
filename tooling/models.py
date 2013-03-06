from django.db import models
from core.models import Build
# Create your models here.
class Tooling(models.Model):
    tooling_id =models.AutoField(primary_key=True);
    ide_platform= models.CharField(max_length=30);
    ipa_test_interpreter = models.NullBooleanField();
    ipa_debug_interpreter = models.NullBooleanField();
    ipa_app_store = models.NullBooleanField();
    ipa_test = models.NullBooleanField();
    ipa_debug = models.NullBooleanField();
    ipa_ad_hoc = models.NullBooleanField();
    ipa_test_interpreter_simulator = models.NullBooleanField();
    ipa_debug_interpreter_simulator = models.NullBooleanField();
    
    deleted_flag=models.NullBooleanField(default=False);
    def __unicode__(self):
        return (self.ide_platform)
    
class ToolingResult(models.Model):
    result_id= models.AutoField(primary_key=True);
    outcome_result=models.BooleanField();
    tooling=models.ForeignKey(Tooling);
    tooling_ide= models.CharField(max_length="30");
    build = models.ForeignKey(Build,);
    build_number=models.CharField(max_length="20");
    target=models.CharField(max_length="20");
    release_number=models.CharField(max_length="30");
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
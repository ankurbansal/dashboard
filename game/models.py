from django.db import models
from core.models import Build, Device

class Game(models.Model):
    game_id= models.AutoField(primary_key=True);
    game_name= models.TextField(max_length=400);
    outcome=models.NullBooleanField();
    cr_dt=models.DateTimeField();
    cr_user=models.CharField(max_length=15);
    lst_dt=models.DateTimeField();
    lst_user=models.CharField(max_length=15);
    deleted_flag=models.NullBooleanField(default=False);
    def primary_key(self):
        return self.game_id
    def __unicode__(self):
        return self.game_name
    
class GameResult(models.Model):
    result_id= models.AutoField(primary_key=True);
    outcome_result=models.BooleanField();
    game=models.ForeignKey(Game);
    game_name= models.CharField(max_length="30");
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
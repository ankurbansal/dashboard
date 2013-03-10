from django.contrib import admin
from game import admin_methods, form
from game.models import Game, GameResult

class GameAdmin(admin.ModelAdmin):
    list_display=('game_name','outcome')
    list_per_page=20;
    ordering=('-game_name',)
    search_fields=['game_name']
    change_list_template="admin/custom_change_list.html"
    actions=[admin_methods.mark_Pass,admin_methods.mark_Fail]
    def changelist_view(self, request, extra_context=None):
        formInfo= form.GameInsertRequest();
        extra_context = {}
        extra_context['input_form']= formInfo;
        return super(GameAdmin, self).changelist_view(request,extra_context)
    
class GamingResultAdmin(admin.ModelAdmin):
    list_display=('game_name',
                  'build_number','device',
                  'outcome_result','release_number','lst_user','lst_dt')
    list_per_page=40;
    actions_on_bottom = True
    ordering=('-lst_dt',)
    
admin.site.register(Game,GameAdmin);
admin.site.register(GameResult,GamingResultAdmin);

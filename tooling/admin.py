from django.contrib import admin
from tooling import admin_methods
from tooling import form
from tooling.models import Tooling, ToolingResult
# Register your models here.
class ToolingAdmin(admin.ModelAdmin):
    list_display=('ide_platform','ipa_test_interpreter','ipa_debug_interpreter','ipa_app_store',
                  'ipa_test','ipa_debug','ipa_ad_hoc','ipa_test_interpreter_simulator','ipa_debug_interpreter_simulator')
    list_per_page=20;
    
    ordering=('-ide_platform',)
#    list_filter=('suite','lst_user','test_area')
    search_fields=['ide_platform']
    change_list_template="admin/custom_change_list.html"
    actions=[admin_methods.mark_Pass,admin_methods.mark_Fail]
    def changelist_view(self, request, extra_context=None):
        formInfo= form.ToolingInsertRequest();
        extra_context = {}
        extra_context['input_form']= formInfo;
        return super(ToolingAdmin, self).changelist_view(request,extra_context)
    
class ResultAdmin(admin.ModelAdmin):
    list_display=('tooling_ide',
                  'build_number',
                  'target','outcome_result','release_number','lst_user','lst_dt')
    list_per_page=40;
    actions_on_bottom = True
    ordering=('-lst_dt',)
    
admin.site.register(Tooling,ToolingAdmin);
admin.site.register(ToolingResult,ResultAdmin);
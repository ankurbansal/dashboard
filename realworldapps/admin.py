from django.contrib import admin
from realworldapps import admin_methods, form
from realworldapps.models import RealWorldApp , RealWorldAppResult

class RealWorldAppAdmin(admin.ModelAdmin):
    list_display=('realworldapp_name','outcome')
    list_per_page=20;
    ordering=('-realworldapp_name',)
    search_fields=['realworldapp_name']
    change_list_template="admin/custom_change_list.html"
    actions=[admin_methods.mark_Pass,admin_methods.mark_Fail]
    def changelist_view(self, request, extra_context=None):
        formInfo= form.RealWorldAppInsertRequest();
        extra_context = {}
        extra_context['input_form']= formInfo;
        return super(RealWorldAppAdmin, self).changelist_view(request,extra_context)
    
class RealWorldAppResultAdmin(admin.ModelAdmin):
    list_display=('realworldapp_name',
                  'build_number','device',
                  'outcome_result','release_number','lst_user','lst_dt')
    list_per_page=40;
    actions_on_bottom = True
    ordering=('-lst_dt',)
    
admin.site.register(RealWorldApp,RealWorldAppAdmin);
admin.site.register(RealWorldAppResult,RealWorldAppResultAdmin);

from django.contrib import admin
from features import admin_methods, form
from features.models import FeatureResult, Features

# Register your models here.
class FeatureAdmin(admin.ModelAdmin):
    list_display=('featureName','outcome','lst_user')
    list_per_page=40;
    actions_on_bottom = True
    ordering=('-featureName',)
    search_fields=['featureName','test_path']
    change_list_template="admin/custom_change_list.html"
    actions=[admin_methods.mark_Pass,admin_methods.mark_Fail]
    def changelist_view(self, request, extra_context=None):
        print request 
        print request
        formInfo= form.FeatureInsertRequest();
        extra_context = {}
        extra_context['input_form']= formInfo;
        return super(FeatureAdmin, self).changelist_view(request,extra_context)
    
    
class FeatureResultAdmin(admin.ModelAdmin):
    list_display=('result_id',
#                  'test_path',
                  'feature_name','build_number','device_info','render_mode','outcome_result','release_number','lst_user','lst_dt')
    list_per_page=40;
    actions_on_bottom = True
    ordering=('-lst_dt',)

admin.site.register(FeatureResult,FeatureResultAdmin);
admin.site.register(Features,FeatureAdmin);
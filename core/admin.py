from django.contrib import admin
from core.models import  TestCase,Build,Device, Result
from core import form
from core import admin_methods


# Register your models here.


class TestCaseAdmin(admin.ModelAdmin):
    list_display=('swfName',
#                  'test_path',
                  'test_area','suite','test_caseid','outcome','lst_user')
    list_per_page=40;
    actions_on_bottom = True
    ordering=('-swfName',)
    list_filter=('suite','lst_user','test_area')
    search_fields=['swfName','test_path']
    change_list_template="admin/custom_change_list.html"
    actions=[admin_methods.mark_Pass,admin_methods.mark_Fail]
    def changelist_view(self, request, extra_context=None):
        print request 
        print request
        formInfo= form.TestCaseInsertRequest();
        extra_context = {}
        extra_context['input_form']= formInfo;
        return super(TestCaseAdmin, self).changelist_view(request,extra_context)
    
    
class ResultAdmin(admin.ModelAdmin):
    list_display=('result_id',
#                  'test_path',
                  'test_case_name','build_number','device_info','render_mode','outcome_result','release_number','lst_user','lst_dt')
    list_per_page=40;
    actions_on_bottom = True
    ordering=('-lst_dt',)


    
admin.site.register(Build);
admin.site.register(Device);
admin.site.register(Result,ResultAdmin);
admin.site.register(TestCase,TestCaseAdmin);


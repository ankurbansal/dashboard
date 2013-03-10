'''
Created on Mar 3, 2013

@author: ankbansa
'''
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from core import form
from core.models import Result
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

def mark(modeladmin,request,queryset,bool_outcome):
   
    if request.method == 'POST': # If the form has been submitted..
        requestForm = form.TestCaseInsertRequest(request.POST) # A form bound to the POST data
        num_testCase=0;
        
        if requestForm.is_valid():
                print "coming in mark";
                requestForm.clean();
                print requestForm;
                release_candidate_number = requestForm.cleaned_data['release_candidate_number'];
                render_mode=requestForm.cleaned_data['render_mode'];
                devices=requestForm.cleaned_data['devices'];
                build=requestForm.cleaned_data['build'];
                print build
                print type(build)
    #            print build.number
                
                print release_candidate_number,render_mode,devices,build;
                for obj in queryset:
                    result = Result();
                    result.render_mode=render_mode;
                    result.release_number=release_candidate_number;
                    result.test_case_name=obj.swfName;
                    result.test_case=obj
                    result.build=build;
                    result.device=devices
                    result.device_info=devices.name+devices.OS_version
                    result.outcome_result=bool_outcome;
                    obj.outcome=bool_outcome;
                    obj.lst_dt=timezone.now().date();
                    result.lst_user=request.user.username;
                    result.build_number=build.number;
                    result.cr_dt=timezone.now().date();
                    result.deleted_flag=False;
                    result.lst_user=request.user.username;
                    result.cr_user=request.user.username;
                    result.lst_dt=timezone.now().date();
                    result.lst_user=request.user.username;
                    num_testCase=num_testCase+1;
                    obj.save();
                    result.save();
                modeladmin.message_user(request, "%s successfully marked as Pass." % num_testCase)
        else:
                print requestForm.errors;
                modeladmin.message_user(request, requestForm.errors.as_text)
                return render_to_response('admin/custom_change_list.html',  {'input_form': requestForm})



def mark_Fail(modeladmin,request,queryset):
    print "coming in mark_Fail ";
    mark(modeladmin,request,queryset,False);   
mark_Fail.short_description="Mark as Fail"


def mark_Pass(modeladmin,request,queryset):
    print "coming in mark_Pass ";
    mark(modeladmin,request,queryset,True);
mark_Pass.short_description="Mark as Pass"   



 
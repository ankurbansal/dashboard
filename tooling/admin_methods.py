'''
Created on Mar 3, 2013

@author: ankbansa
'''
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from tooling import form
from tooling.models import ToolingResult
from django.utils import timezone




def mark(modeladmin,request,queryset,bool_outcome):
   
    if request.method == 'POST': # If the form has been submitted...
        requestForm = form.ToolingInsertRequest(request.POST) # A form bound to the POST data
        if requestForm.is_valid():
            requestForm.clean();
             
            
#            print requestForm;
            release_candidate_number = requestForm.cleaned_data['release_candidate_number'];
            target=requestForm.cleaned_data['target'];
            devices=requestForm.cleaned_data['devices'];
            build=requestForm.cleaned_data['build'];
          
#            print build
#            print type(build)
#            print build.number
            num_testCase=0;
#            print release_candidate_number,target,devices,build;
            for obj in queryset:
                print obj
                result = ToolingResult();
                result.release_number=release_candidate_number;
                result.tooling_ide=obj.ide_platform;
                result.tooling=obj
                result.build=build;
                result.outcome_result=bool_outcome;
#                obj.outcome=bool_outcome;
#                obj.lst_dt=timezone.now().date();
                result.lst_user=request.user.username;
                result.build_number=build.number;
                result.cr_dt=timezone.now().date();
                result.deleted_flag=False;
                result.lst_user=request.user.username;
                result.cr_user=request.user.username;
                result.lst_dt=timezone.now().date();
                result.lst_user=request.user.username;
                num_testCase=num_testCase+1;
                #f for loop  target 
                for tmpTarget in target:
                    print tmpTarget
                    if tmpTarget == "ipa_test_interpreter":
                        obj.ipa_test_interpreter=bool_outcome;
                        result.target+=' ' + 'ipa_test_interpreter'
                    if tmpTarget == "ipa_debug_interpreter":
                        obj.ipa_debug_interpreter=bool_outcome; 
                        result.target+=' ' + 'ipa_debug_interpreter'  
                    if tmpTarget == "ipa_test":
                        obj.ipa_test=bool_outcome;
                        result.target+=' ' + 'ipa_test'
                    if tmpTarget == "ipa_debug":
                        obj.ipa_debug=bool_outcome;
                        result.target+=' ' + 'ipa_debug'
                    if tmpTarget == "ipa_app_store":
                        obj.ipa_app_store=bool_outcome;
                        result.target+=' ' + 'ipa_app_store'
                    if tmpTarget == "ipa_ad_hoc":
                        obj.ipa_ad_hoc=bool_outcome;
                        result.target+=' ' + 'ipa_ad_hoc'
                    if tmpTarget == "ipa_test_interpreter_simulator":
                        obj.ipa_test_interpreter_simulator=bool_outcome;
                        result.target+=' ' + 'ipa_test_interpreter_simulator'
                    if tmpTarget == "ipa_debug_interpreter_simulator":
                        obj.ipa_debug_interpreter_simulator=bool_outcome;
                        result.target+=' ' + 'ipa_debug_interpreter_simulator'
                obj.save();
                result.save();
                modeladmin.message_user(request, "%s successfully marked as Pass." % num_testCase)
                
                
            
     





def mark_Fail(modeladmin,request,queryset):
    print "coming in mark_Fail ";
    mark(modeladmin,request,queryset,False);   
mark_Fail.short_description="Mark as Fail"


def mark_Pass(modeladmin,request,queryset):
    print "coming in mark_Pass ";
    mark(modeladmin,request,queryset,True);
mark_Pass.short_description="Mark as Pass"   



 
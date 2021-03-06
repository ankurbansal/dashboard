from django import forms
from core.models import Device, Build


class ToolingInsertRequest(forms.Form):
    target=(
        (u'ipa_test_interpreter',u'ipa-test-interpreter'),
        (u'ipa_debug_interpreter',u'ipa-debug-interpreter'),
        (u'ipa_debug',u'ipa-debug'),
        (u'ipa_app_store',u'ipa-app-store'),
        (u'ipa_test',u'ipa-test'),
        (u'ipa_ad_hoc',u'ipa-ad-hoc'),
        (u'ipa_debug_interpreter_simulator',u'ipa-debug-interpreter-simulator'),
        (u'ipa_test_interpreter_simulator',u'ipa-debug-interpreter-simulator'),

    )
    release_candidate_number= forms.CharField(max_length="15");
    target = forms.MultipleChoiceField(choices=target,label="target");
    devices=forms.ModelMultipleChoiceField(queryset=Device.objects.all());
    build=forms.ModelChoiceField(queryset=Build.objects.all());
    
    
    
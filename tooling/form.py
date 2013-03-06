from django import forms
from core.models import Device, Build


class ToolingInsertRequest(forms.Form):
    target=(
        (u'ipa_test_interpreter',u'ipa-test-interpreter'),
        (u'ipa_debug_interpreter',u'ipa-debug-interpreter'),
    )
    release_candidate_number= forms.CharField(max_length="15");
    target = forms.MultipleChoiceField(choices=target,label="target");
    devices=forms.ModelMultipleChoiceField(queryset=Device.objects.all());
    build=forms.ModelChoiceField(queryset=Build.objects.all());
    
    
    
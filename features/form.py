from django import forms
from core.models import Device, Build


class FeatureInsertRequest(forms.Form):
    RENDER_MODE=(
        (u'CPU',u'cpu'),
        (u'GPU',u'gpu'),
        (u'DIRECT',u'direct'),
    )
    release_candidate_number= forms.CharField(max_length="15");
    render_mode = forms.ChoiceField(choices=RENDER_MODE,label="render mode");
    devices=forms.ModelChoiceField(queryset=Device.objects.all());
    build=forms.ModelChoiceField(queryset=Build.objects.all());
    
    
    
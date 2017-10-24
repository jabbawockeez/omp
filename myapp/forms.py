from django import forms

class DeployForm(forms.Form):
    svn_url = forms.URLField()
    jar_server_ip = forms.GenericIPAddressField()
    cwar_server_ip = forms.GenericIPAddressField(required = False)
    awar_server_ip = forms.GenericIPAddressField(required = False)
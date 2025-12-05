from django import forms

from apps.company.models import CustomerBranch


class CustomerBranchForm(forms.ModelForm):
    class Meta:
        model = CustomerBranch
        fields = ['name', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': "input input-bordered w-full"})

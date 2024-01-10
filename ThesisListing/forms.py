from django import forms
from .models import thesis_listings,institutes
from dynamic_forms import DynamicField,DynamicFormMixin


class ThesisForm(DynamicFormMixin,forms.ModelForm):
    class Meta:
        model = thesis_listings
        fields = ['supervisor','title', 'description','writing_language','student_level','department','institute','additional_information','contact','accompanying_file']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['institute'].queryset =institutes.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['institute'].queryset = institutes.objects.filter(department_id=department_id).order_by('institute_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['institute'].queryset = self.instance.department.institute_set.order_by('institute_name')

   
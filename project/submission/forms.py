from django import forms

from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = ['team']

    def clean_image(self):
        zip_file = self.cleaned_data.get('zipped_submission', False)
        if zip_file:
            if zip_file._size > 1*1024*1024:
                raise forms.ValidationError("Zip file too large ( > 1mb )")
            return zip_file
        else:
            raise forms.ValidationError("Couldn't read uploaded zip.")

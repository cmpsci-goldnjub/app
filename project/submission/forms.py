from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import FileSubmission, VideoSubmission


class VideoSubmissionForm(forms.ModelForm):

    class Meta:
        model = VideoSubmission
        fields = ['video_url']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(VideoSubmissionForm, self).__init__(*args, **kwargs)


class FileSubmissionForm(forms.ModelForm):

    class Meta:
        model = FileSubmission
        fields = ['submission', 'comments']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(FileSubmissionForm, self).__init__(*args, **kwargs)

    def clean_submission(self):
        submission = self.cleaned_data.get('submission', False)
        if submission:
            if submission._size > 1024**3:
                raise forms.ValidationError("Submission file too large ( > 1 GB )")
            return submission
        else:
            raise forms.ValidationError("Couldn't read uploaded zip.")

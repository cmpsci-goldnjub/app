from django.db import models
from django.core.validators import MaxLengthValidator

from project.teams.models import Team


class Submission(models.Model):

    class Meta:
        ordering = ['created']
        get_latest_by = "created"

    team = models.ForeignKey(Team)

    created = models.DateTimeField(auto_now_add=True)

    video_url = models.URLField()

    zipped_submission = models.FileField()

    description = models.TextField(blank=True, validators=[MaxLengthValidator(1000)],
                                   help_text="Any last-minute comments? Don't forget you should have a README!")

from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxLengthValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

import bleach
import markdown
import uuid

name_validator = RegexValidator(
    regex=r"[a-zA-Z0-9_\-.: ]+",
    message="Names can contain letters, numbers, dashes, periods, colons, and whitespace."
)


description_length_validator = MaxLengthValidator(2000)


def slug_validator(value):
    slug = slugify(value)
    if not slugify(value):
        raise ValidationError('Please add some more characters to your team name.')
    if Team.objects.filter(slug=slug).exists():
        raise ValidationError('A team with a similar name exists.')


def ascii_validator(value):
    try:
        value.encode('ascii')
    except UnicodeEncodeError:
        raise ValidationError('Team name should contain only ASCII characters.')


class TeamFullException(Exception):
    pass


class Team(models.Model):

    class Meta:
        ordering = ['name']
        get_latest_by = "created"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, null=False)

    name = models.CharField(max_length=50, validators=[name_validator, ascii_validator, slug_validator],
                            help_text="Your team's project name!")
    description = models.TextField(blank=True, validators=[description_length_validator],
                                   help_text="Tell us about your project! Or don't. It's up to you!")
    rendered_description = models.TextField(editable=False)

    members = models.ManyToManyField(User)

    created = models.DateTimeField(auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        kwds = {'slug': self.slug}
        return ('team_detail', (), kwds)

    def __str__(self):
        return self.name

    def is_full(self):
        return self.members.count() >= 5

    def add_member(self, user):
        if not self.is_full():
            return self.members.add(user)
        raise TeamFullException()


class Request(models.Model):

    class Meta:
        ordering = ['created']
        get_latest_by = "created"

    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)

    created = models.DateTimeField(auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        kwds = {'pk': self.pk}
        return ('request_response', (), kwds)

    def __str__(self):
        return u"Request for {} to join {}".format(self.user.username,
                                                   self.team.name)

@receiver(pre_save, sender=Team)
def team_pre_save(sender, instance, **kwargs):
    """Called before a Team is saved
    - Sets slug according to name
    - Renders description field
    """
    instance.slug = slugify(instance.name)

    rendered = markdown.markdown(instance.description, safe_mode='escape')
    clean_rendered = bleach.clean(rendered,
                                  tags=settings.ALLOWED_HTML_TAGS,
                                  attributes=settings.ALLOWED_HTML_ATTRS)
    instance.rendered_description = clean_rendered

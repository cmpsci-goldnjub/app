from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

import bleach
import markdown

name_validator = RegexValidator(
    regex=r"[\w\-.:\s]+",
    message="Names can contain letters, numbers, dashes, periods, colons, and whitespace."
)

class Team(models.Model):

    class Meta:
        ordering = ['name']
        get_latest_by = "created"

    slug = models.SlugField(primary_key=True)

    name = models.CharField(max_length=50, validators=[name_validator],
                            help_text="Your team's project name!")
    description = models.TextField(blank=True,
                                   help_text="Tell us about your project! Or don't. It's up to you!")
    rendered_description = models.TextField(editable=False)

    members = models.ManyToManyField(User)

    created = models.DateTimeField(auto_now_add=True)

    @models.permalink
    def get_absolute_url(self):
        kwds = {'slug': self.slug}
        return ('team_detail', (), kwds)


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

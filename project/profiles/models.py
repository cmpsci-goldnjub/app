from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxLengthValidator

import markdown
import bleach


class Profile(models.Model):
    CS_STUDENT = 'css'
    STUDENT = 'stu'
    STAFF_FACULTY = 'fac'
    ALUMNI = 'alm'
    STATUS_CHOICES = (
        (CS_STUDENT, 'Missouri S&T Computer Science Student'),
        (STUDENT, 'Missouri S&T Student'),
        (STAFF_FACULTY, 'Missouri S&T Staff or Faculty'),
        (ALUMNI, 'Missour S&T Alumnus/Alumna'),
    )

    user = models.OneToOneField(User, related_name="profile")
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=STUDENT)
    about_me = models.TextField(validators=[MaxLengthValidator(500)])
    rendered_about_me = models.TextField(editable=False)

    @models.permalink
    def get_absolute_url(self):
        return ('view_profile', (), {'username': self.user.username})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=Profile)
def user_profile_pre_save(sender, instance, **kwargs):
    # Render the about_me field as HTML instead of markdown
    rendered = markdown.markdown(instance.about_me, safe_mode='escape')
    clean_rendered = bleach.clean(rendered,
                                  tags=settings.ALLOWED_HTML_TAGS,
                                  attributes=settings.ALLOWED_HTML_ATTRS)
    instance.rendered_about_me = clean_rendered

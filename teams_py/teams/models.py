from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import Human


class Team(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Human, related_name='team', blank=True)

    def __str__(self) -> str:
        return str([self.name, self.members])

    class Meta:
        verbose_name = _("team")
        verbose_name_plural = _("teams")



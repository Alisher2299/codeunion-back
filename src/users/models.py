from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from common.models.abstract import (
    PhoneNumberBaseModel,
    TimeStampedModel,
    ActivationBaseModel,
)
from .managers import UserManager

GENDER_CHOICES = (("empty", _("Empty")), ("man", _("Man")), ("woman", _("Woman")))


class User(AbstractUser, PhoneNumberBaseModel, TimeStampedModel, ActivationBaseModel):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, blank=True, default='', max_length=150)
    phone_confirm = models.BooleanField(_("Phone confirmed?"), default=False)
    phone_region = models.CharField(_("Phone region by ISO2 standard"), default="KZ", max_length=2)
    birth_date = models.DateField(_("Birth date"), null=True, blank=True)
    gender = models.CharField(_("Gender"), choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0], max_length=5)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-created"]

    def __str__(self):
        fields = [self.phone_number, self.email, self.first_name, self.last_name]
        fields = list(filter(lambda x: x, fields))
        fields = list(map(lambda x: str(x), fields))

        return " | ".join(fields)


# ABSTRACT CLASSES


class UserableBaseModel(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), related_name="%(class)s", on_delete=models.PROTECT)

    class Meta:
        abstract = True

# ABSTRACT CLASSES END

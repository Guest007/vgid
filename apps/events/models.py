from django.db import models
from core.models import ParentModel
from django.utils.translation import ugettext, ugettext_lazy as _


class Event(ParentModel):
    """
    main Event model for current news and for past events
    """
    image = models.ImageField(_("Image"), upload_to='enents')


class Section(models.Model):
    pass

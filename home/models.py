from django.db import models

from wagtail.core.models import Page
from .tasks import count_hompage


class HomePage(Page):
    pass

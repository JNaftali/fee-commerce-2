from django.db import models
from wagtail import images
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images import edit_handlers as image_edit_handlers
from wagtail.search import index


class HomePage(Page):
    subtitle = RichTextField(verbose_name="Subtitle", default="")
    background = models.ForeignKey(
        to=images.get_image_model_string(),
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Background",
        null=True,
    )

    hero_panels = [
        FieldPanel("subtitle"),
        image_edit_handlers.ImageChooserPanel("background"),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel(heading="Hero", children=hero_panels),
    ]

    preview_modes = []

    class Meta:
        verbose_name = "Homepage"

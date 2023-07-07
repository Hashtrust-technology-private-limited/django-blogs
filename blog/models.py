from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def upload_location(instance, filename, *args, **kwargs):
    file_path = "blog/{author_id}/{title}-{filename}".format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path


class BlogState(models.TextChoices):
    draft = (
        "draft",
        _("Draft"),
    )

    published = (
        "published",
        _("Published"),
    )


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class Blog(CreatedUpdatedMixin):
    title = models.CharField(max_length=60)
    content = models.TextField(_("Add Blog Content"))
    short_description = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=30, choices=BlogState.choices)
    attachment = models.FileField(upload_to=upload_location)

    def __str__(self):
        return self.title

    @property
    def read_time(self):
        words_per_minute = 200
        read_time_minutes = len(self.content.split()) / words_per_minute
        read_time_minutes = round(read_time_minutes)
        return f"{read_time_minutes} min read"

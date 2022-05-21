import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FilmWork(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("title"), max_length=150)
    description = models.TextField(_("description"), null=True, blank=True)
    creation_date = models.DateField(
        _("creation_date"),
        null=True,
        blank=True,
    )
    certificate = models.TextField(_("certificate"), null=True, blank=True)
    file_path = models.FileField(
        _("file_path"), upload_to="film_works/", null=True, blank=True
    )
    rating = models.FloatField(
        _("rating"),
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        null=True,
        blank=True,
    )
    type = models.CharField(_("type"), max_length=20, null=True, blank=True)
    person = models.ManyToManyField("Person", through="PersonFilmWork")
    genre = models.ManyToManyField("Genre", through="GenreFilmWork")

    class Meta:
        verbose_name = _("film_work")
        verbose_name_plural = _("film_work")

        db_table = 'content"."film_work'


class Genre(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"), null=True, blank=True)

    class Meta:
        verbose_name = _("genre")
        verbose_name_plural = _("genres")
        db_table = 'content"."genre'


class Person(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(_("full_name"), max_length=100)
    birth_date = models.DateField(_("birth_date"), null=True, blank=True)

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("persons")
        db_table = 'content"."person'


class GenreFilmWork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey(FilmWork, to_field="id", on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, to_field="id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("genre_film_work")
        verbose_name_plural = _("genre_film_works")
        constraints = [
            models.UniqueConstraint(
                fields=["film_work_id", "genre_id"], name="film_work_genre"
            )
        ]
        indexes = [
            models.Index(fields=("film_work_id", "genre_id"), name="film_work_genre")
        ]
        db_table = 'content"."genre_film_work'


class PersonFilmWorkRoles(models.TextChoices):
    Actor = "actor", _("Actor")
    Writer = "writer", _("Writer")
    Director = "director", _("Director")


class PersonFilmWork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey(FilmWork, to_field="id", on_delete=models.CASCADE)
    person = models.ForeignKey(Person, to_field="id", on_delete=models.CASCADE)
    role = models.CharField(
        _("role"), max_length=20, choices=PersonFilmWorkRoles.choices
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("person_film_work")
        verbose_name_plural = _("person_film_works")
        constraints = [
            models.UniqueConstraint(
                fields=["film_work_id", "person_id", "role"], name="film_work_person"
            )
        ]
        indexes = [
            models.Index(
                fields=("film_work_id", "person_id", "role"), name="film_work_person"
            )
        ]
        db_table = 'content"."person_film_work'

from django.contrib import admin

from .models import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork


class PersonInline(admin.TabularInline):
    model = PersonFilmWork
    extra = 1


class GenreInline(admin.TabularInline):
    model = GenreFilmWork
    extra = 1


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'rating', 'created_at', 'updated_at')
    # Модели связей
    inlines = (PersonInline, GenreInline,)

    fields = (
        'title', 'type', 'description', 'creation_date', 'certificate',
        'file_path', 'rating',
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

    fields = (
        'name', 'description',
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date',)

    fields = (
        'full_name', 'birth_date',
    )



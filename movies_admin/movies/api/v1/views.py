from decimal import Decimal

from django.contrib.postgres.aggregates import ArrayAgg
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from ...models import FilmWork, PersonFilmWorkRoles


class MyDjangoJSONEncoder(DjangoJSONEncoder):
    """
    Класс кастомный сериаллизатор json,
    используется так как стандартный сериализатор мутирует Decimal в str
    """

    def default(self, object):
        if isinstance(object, Decimal):
            return float(object)
        return super().default(object)


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ["get"]

    def get_queryset(self):
        film_work = FilmWork.objects.values(
            "id", "title", "description", "creation_date", "rating", "type"
        ).annotate(
            genres=ArrayAgg("genre__name", distinct=True),
            actors=self._aggregate_person(role=PersonFilmWorkRoles.Actor),
            directors=self._aggregate_person(role=PersonFilmWorkRoles.Director),
            writers=self._aggregate_person(role=PersonFilmWorkRoles.Writer),
        )
        return film_work

    @staticmethod
    def _aggregate_person(role):
        result = ArrayAgg(
            "person__full_name", filter=Q(personfilmwork__role=role), distinct=True
        )
        return result

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, encoder=MyDjangoJSONEncoder)


class MoviesListApi(MoviesApiMixin, BaseListView):
    def get_context_data(self, **kwargs):
        queryset = self.get_queryset().order_by("id")
        panginate_by = 50
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset, panginate_by
        )
        if is_paginated:
            context = {
                "count": paginator.count,
                "total_pages": paginator.num_pages,
                "prev": page.previous_page_number() if page.has_previous() else None,
                "next": page.next_page_number() if page.has_next() else None,
                "results": list(page),
            }
            return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        return kwargs["object"]

from decimal import Decimal

from django.contrib.postgres.aggregates import ArrayAgg
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder

from movies.models import FilmWork


# Для конвертации float в float при сериализации Json
class MyDjangoJSONEncoder(DjangoJSONEncoder):
    def default(self, object):
        if isinstance(object, Decimal):
            return float(object)
        return super().default(object)


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    def get_queryset(self):
        film_work = FilmWork.objects.values('id', 'title', 'description', 'creation_date', 'rating', 'type') \
            .annotate(genres=ArrayAgg('genre__name', distinct=True),
                      actors=ArrayAgg('person__full_name', filter=Q(
                          personfilmwork__role='actor'), distinct=True),
                      directors=ArrayAgg('person__full_name', filter=Q(
                          personfilmwork__role='director'), distinct=True),
                      writers=ArrayAgg('person__full_name', filter=Q(
                          personfilmwork__role='writer'), distinct=True), )
        return film_work

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, encoder=MyDjangoJSONEncoder)


class MoviesListApi(MoviesApiMixin, BaseListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset().order_by('id')
        panginate_by = 50
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            panginate_by
        )
        if is_paginated:
            context = {
                'count': paginator.count,
                'total_pages': paginator.num_pages,
                'prev': page.previous_page_number() if page.has_previous() else None,
                'next': page.next_page_number() if page.has_next() else None,
                'results': list(page)
            }
            return context


class MoviesDetailApi(MoviesApiMixin, BaseListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        uuid_pk = self.kwargs['pk']
        context = self.get_queryset().get(id=uuid_pk)

        return context

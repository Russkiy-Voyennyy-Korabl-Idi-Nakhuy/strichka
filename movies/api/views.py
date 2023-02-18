from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from movies.models import Cast, Category, Collection, Country, Movie, StreamingPlatform
from movies.serializers import (
    CastSerializer,
    CategorySerializer,
    CollectionSerializer,
    CountrySerializer,
    MovieSerializer,
    StreamingPlatformSerializer,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CastViewSet(ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["place_of_birth", "birthday"]
    search_fields = ["=imdb_id", "full_name"]


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["name"]
    search_fields = ["name", "code"]


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().prefetch_related(
        "directors", "writers", "actors", "categories", "country"
    )
    serializer_class = MovieSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["year", "age_mark", "is_movie"]
    search_fields = ["=imdb_id", "title"]
    ordering_fields = ["year", "imdb_rate", "imdb_votes"]


class StreamingPlatformViewSet(ModelViewSet):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["service", "video_format", "purchase_type", "movie__year"]
    search_fields = ["=service", "=movie__imdb_id"]
    ordering_fields = [
        "video_format",
        "purchase_type",
        "movie__year",
        "movie__imdb_rate",
        "movie__imdb_votes",
    ]


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name"]

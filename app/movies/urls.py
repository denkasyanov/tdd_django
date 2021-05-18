from django.conf.urls import url
from django.urls import include, path

from .views import MovieViewSet  #, MovieList, MovieDetail

from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet)


urlpatterns = [
    # path("api/movies/", MovieList.as_view()),
    # path("api/movies/<int:pk>/", MovieDetail.as_view()),
    path('api/', include(router.urls)),
]

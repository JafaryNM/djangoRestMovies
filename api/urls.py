from django.urls import path
#from .views import movies_list,movies_detail
from .views import MovieDetailAV,MovieListAV


urlpatterns=[
    path('api/', MovieListAV.as_view(),name='api_list' ),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie_details')
]
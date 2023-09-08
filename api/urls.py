from django.urls import path
#from .views import movies_list,movies_detail
from .views import WatchListAV,WatchMovieDetailAV,StreamPlatformDetailAV,StreamPlatformListAV


urlpatterns=[
    path('api/', WatchListAV.as_view(),name='api_list' ),
    path('<int:pk>', StreamPlatformDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream_list'),
  
    
]
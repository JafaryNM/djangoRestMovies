from django.urls import path
#from .views import movies_list,movies_detail
from .views import WatchListAV,WatchMovieDetailAV,StreamPlatformDetailAV,StreamPlatformListAV,ReviewList,ReviewDetail


urlpatterns=[
    path('api/', WatchListAV.as_view(),name='api_list' ),
    path('<int:pk>', WatchListAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream_list'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='stream_detai'),
    path('review/',ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>',ReviewDetail.as_view(), name='review_detail'),
    
]
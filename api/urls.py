from django.urls import path,include
#from .views import movies_list,
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import WatchListAV,WatchMovieDetailAV,StreamPlatformDetailAV,StreamPlatformListAV,ReviewList,ReviewDetail,StreamPlatformVS,ReviewCreate
=======
from .views import WatchListAV,WatchMovieDetailAV,StreamPlatformDetailAV,StreamPlatformVS,ReviewList,ReviewDetail,ReviewCreate
>>>>>>> 7f8a07826bb2de6e8d98c0272d59484f74cbe5c8


router=DefaultRouter()

router.register('stream',StreamPlatformVS, basename='stream')

urlpatterns=[
    path('api/', WatchListAV.as_view(),name='api_list' ),
    path('<int:pk>', WatchListAV.as_view(), name='movie_details'),
    
    #path('stream/', StreamPlatformListAV.as_view(), name='stream_list'),
    #path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='stream_detai'),
    
    path('', include(router.urls)),
    
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review',ReviewList.as_view(), name='stream_detai'), 
   
   
    path('stream/review/<int:pk>',ReviewDetail.as_view(), name='review_detail'),
    
]
from django.urls import path
from .views import movies_list,movies_detail


urlpatterns=[
    path('api/', movies_list,name='api_list' ),
    path('<int:pk>', movies_detail, name='movie_details')
]
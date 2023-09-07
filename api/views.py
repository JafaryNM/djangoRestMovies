from django.shortcuts import render
from watchlist_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# Retrive all data

@api_view()
def movies_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)


# Retrive individual data 

@api_view()

def movies_detail(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)